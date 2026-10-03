import copy, json, math, pathlib, sys, tempfile, unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import pipeline
import gates

class ProbeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config=pipeline.read_json(pipeline.ROOT/'probe.json')
        cls.ir=pipeline.build(pipeline.ROOT/'probe.json')

    def changed(self,key,value):
        c=copy.deepcopy(self.config);c['assumptions'][key]['value']=value
        with tempfile.TemporaryDirectory() as directory:
            f=pathlib.Path(directory)/'changed.json';pipeline.write_json(f,c)
            return pipeline.build(f)

    def test_all_observed_claims_resolve_to_cached_evidence(self):
        datasets={}
        for claim in self.ir['claims'].values():
            if claim['kind']!='observed':continue
            source=claim['source_id'];record=self.ir['sources'][source]
            self.assertEqual(record['status'],'ok')
            if source not in datasets:
                body=(pipeline.ROOT/record['cache_path']).read_bytes()
                if source=='mta_stations_official':
                    import csv,io
                    datasets[source]=list(csv.DictReader(io.StringIO(body.decode())))
                else:datasets[source]=json.loads(body)
            loc=claim['locator'];data=datasets[source]
            if 'operation' in loc:expected=len(data)
            else:expected=data[loc['row']][loc.get('field') or loc['column']]
            if isinstance(claim['value'],(int,float)) and not isinstance(claim['value'],bool):
                self.assertAlmostEqual(claim['value'],float(expected))
            else:self.assertEqual(claim['value'],expected)

    def test_no_unknown_gate_is_cleared(self):
        for dossier in self.ir['dossiers']:
            for gate in dossier['gates'].values():
                self.assertEqual(gate['status'],'unknown')
                claim=self.ir['claims'][gate['claim_id']]
                self.assertEqual(claim['kind'],'unknown');self.assertIsNone(claim['value'])

    def test_export_backpressure_preserves_review_access(self):
        self.assertTrue(gates.eligibility(self.ir,'advisor-review','2028710002')['allowed'])
        blocked=gates.eligibility(self.ir,'public-site-proposal','2028710002')
        self.assertFalse(blocked['allowed'])
        self.assertEqual(set(blocked['blocking_gates']),set(self.config['required_gates']))

    def test_rank_and_public_facility_challenge_are_preserved(self):
        self.assertEqual(len(self.ir['screen']['shortlist']),10)
        self.assertEqual(len(self.ir['dossiers']),3)
        dispositions={d['bbl']:d['review']['disposition'] for d in self.ir['dossiers']}
        self.assertEqual(dispositions['2028430040'],'Exclude from ordinary private redevelopment shortlist')
        self.assertEqual(dispositions['2024890077'],'Exclude from ordinary private redevelopment shortlist')
        self.assertEqual(self.ir['lead_decision']['bbl'],'2028710002')

    def test_scenario_debt_coverage_identity(self):
        a=self.config['assumptions'];get=lambda k:a[k]['value']
        for d in self.ir['dossiers']:
            for s in d['scenarios']:
                p=s['claim_prefix'];v=lambda k:self.ir['claims'][p+'.'+k]['value']
                annual_noi=v('debt_support_rent_month')*v('units')*12*(1-get('vacancy_share'))*(1-get('opex_share_egi'))
                self.assertAlmostEqual(annual_noi/v('annual_debt_service'),get('dscr'))
                self.assertLessEqual(v('units')*get('avg_net_unit_sf'),v('net_sf'))
                self.assertGreater((v('units')+1)*get('avg_net_unit_sf'),v('net_sf'))

    def test_cost_sensitivity_does_not_change_units(self):
        changed=self.changed('hard_cost_per_gsf',525)
        p='scenario.2028710002.A.'
        self.assertEqual(changed['claims'][p+'units']['value'],self.ir['claims'][p+'units']['value'])
        self.assertAlmostEqual(changed['claims'][p+'ex_land_cost']['value']/self.ir['claims'][p+'ex_land_cost']['value'],1.5)
        self.assertAlmostEqual(changed['claims'][p+'debt_support_rent_month']['value']/self.ir['claims'][p+'debt_support_rent_month']['value'],1.5)

    def test_larger_home_assumption_propagates(self):
        changed=self.changed('avg_net_unit_sf',1000)
        p='scenario.2028710002.A.'
        self.assertLess(changed['claims'][p+'units']['value'],self.ir['claims'][p+'units']['value'])
        self.assertGreater(changed['claims'][p+'debt_support_rent_month']['value'],self.ir['claims'][p+'debt_support_rent_month']['value'])

    def test_incomplete_scope_is_rejected(self):
        c=copy.deepcopy(self.config);c['scope']['radius_m']['value']=2000
        g=pipeline.Graph(c,pipeline.ROOT/'probe.json')
        with self.assertRaisesRegex(ValueError,'Radius exceeds'):pipeline.screen(c,g)
        c['scope']['station_id']='217';c['scope']['route']='D';c['scope']['radius_m']['value']=650;g=pipeline.Graph(c,pipeline.ROOT/'probe.json')
        with self.assertRaisesRegex(ValueError,'Cached universe'):pipeline.screen(c,g)

    def test_invalid_dsl_is_rejected(self):
        c=copy.deepcopy(self.config);c['screen']['ranking']='opaque-ai-score'
        with self.assertRaises(ValueError):pipeline.validate_config(c)
        c=copy.deepcopy(self.config);c['assumptions']['debt_ltc']['value']=1.5
        with self.assertRaises(ValueError):pipeline.validate_config(c)

    def test_replay_is_deterministic(self):
        replay=pipeline.build(pipeline.ROOT/'probe.json')
        self.assertEqual(json.dumps(self.ir,sort_keys=True),json.dumps(replay,sort_keys=True))

if __name__=='__main__':unittest.main()

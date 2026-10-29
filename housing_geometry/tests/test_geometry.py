import copy
from pathlib import Path
import shutil
import tempfile
import unittest
from housing_workflow.contracts import digest, load, save
from housing_geometry import engine, sources
from housing_geometry.model import compile_model, polygon
from housing_geometry.exports import exports

ROOT=engine.ROOT
SOURCE=ROOT/'examples/geometry-inputs/parcel-source'
ANALYSIS=ROOT/'examples/analysis-recipe/base'
IR=load(ANALYSIS/'ir.json');SHA=digest((ANALYSIS/'ir.json').read_bytes())
MISMATCH=load(ROOT/'examples/geometry-inputs/all-nonresidential-ground.json')
MATCH=load(ROOT/'examples/geometry-inputs/mixed-ground-allocation.json')


def compile(scenario=MATCH,source=SOURCE,analysis=IR,sha=SHA):
    return compile_model(copy.deepcopy(scenario),source,copy.deepcopy(analysis),sha)


def alter_source(root,mutator):
    shutil.copytree(SOURCE,root);data=load(root/'parcel.json');mutator(data);save(root/'parcel.json',data)
    r=load(root/'receipt.json');raw=(root/'parcel.json').read_bytes();r['files']['parcel.json'].update(sha256=digest(raw),bytes=len(raw));save(root/'receipt.json',r)
    return root

class Geometry(unittest.TestCase):
    def test_actual_parcel_identity_versions_and_area_discrepancy_preserved(self):
        ir=compile();s=ir['source_geometry']
        self.assertEqual(s['bbl'],'2028710002');self.assertEqual(s['source_version'],'26v2')
        self.assertEqual(s['recorded_lot_area_sf'],59050)
        self.assertAlmostEqual(s['mapped_polygon_area_sf'],59891.25230980584,places=4)
        self.assertAlmostEqual(s['mapped_minus_recorded_sf'],841.25230980584,places=4)
        self.assertEqual(s['comparison_status'],'unreconciled_source_observations')
    def test_total_match_does_not_hide_program_mismatch(self):
        ir=compile(MISMATCH);checks={c['quantity']:c for c in ir['comparisons']}
        self.assertEqual(checks['gross']['status'],'consistent_within_tolerance')
        self.assertEqual(checks['nonresidential']['difference_sf'],1500)
        self.assertEqual(checks['residential']['difference_sf'],-1500)
        h=__import__('json').loads(exports(ir)['visual-handoff.json'])
        self.assertFalse(h['eligible_as_schematic_reference']);self.assertIsNone(h['prompt'])
        self.assertEqual(ir['visual_handoff_status'],'blocked_area_mismatch')
    def test_explicit_allocation_matches_but_no_professional_gate_clears(self):
        ir=compile()
        self.assertEqual(ir['totals_sf'],{'gross':40000,'nonresidential':6000,'residential':34000})
        self.assertEqual(ir['total_height_ft'],64)
        self.assertEqual(len(ir['floors']),6)
        self.assertTrue(all(c['status']=='consistent_within_tolerance' for c in ir['comparisons']))
        self.assertEqual(set(ir['review_gates'].values()),{'unknown'})
        self.assertEqual(ir['visual_handoff_status'],'schematic_reference_only')
    def test_height_changes_geometry_not_area(self):
        a=compile();s=copy.deepcopy(MATCH);s['floors'][0]['height_ft']['value']=16;b=compile(s)
        self.assertEqual(a['totals_sf'],b['totals_sf']);self.assertEqual(b['total_height_ft'],66)
        self.assertNotEqual(exports(a)['massing.obj'],exports(b)['massing.obj'])
        self.assertNotEqual(exports(a)['visual-handoff.json'],exports(b)['visual-handoff.json'])
    def test_floor_count_changes_mesh_area_and_handoff(self):
        s=copy.deepcopy(MATCH);s['floors'].pop();ir=compile(s)
        self.assertEqual(ir['totals_sf']['gross'],33500)
        self.assertEqual(ir['visual_handoff_status'],'blocked_area_mismatch')
    def test_dimension_changes_recompute_all_quantities(self):
        s=copy.deepcopy(MATCH)
        for f in s['floors']:
            for p in f['footprint']['vertices_ft']:
                if p[1]>350:p[1]+=10
        ir=compile(s)
        self.assertEqual(ir['totals_sf']['gross'],44000)
        self.assertEqual(ir['visual_handoff_status'],'blocked_area_mismatch')
    def test_incompatible_analysis_area_definition_blocks(self):
        for unit in ['net sf','zoning FAR']:
            a=copy.deepcopy(IR);next(c for c in a['claims'] if c['id']=='scenario.gross_area_sf')['unit']=unit
            with self.assertRaisesRegex(ValueError,'incompatible'):compile(analysis=a)
    def test_wrong_parcel_or_source_hash_blocks(self):
        s=copy.deepcopy(MATCH);s['site_bbl']='2028560051'
        with self.assertRaisesRegex(ValueError,'parcel mismatch'):compile(s)
        s=copy.deepcopy(MATCH);s['parcel_geometry_sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'different source'):compile(s)
    def test_invalid_open_or_self_intersecting_polygon_blocks(self):
        for pts in [[[0,0],[5,0],[5,5],[0,5]],[[0,0],[5,5],[0,5],[5,0],[0,0]],[[0,0],[True,0],[5,5],[0,0]]]:
            with self.assertRaises(ValueError):polygon(pts)
    def test_outside_or_unsupported_cantilever_blocks(self):
        s=copy.deepcopy(MATCH)
        for p in s['floors'][0]['footprint']['vertices_ft']:p[0]+=1000
        with self.assertRaisesRegex(ValueError,'boundary'):compile(s)
        s=copy.deepcopy(MATCH)
        for p in s['floors'][1]['footprint']['vertices_ft']:p[0]+=6
        with self.assertRaisesRegex(ValueError,'Upper plate'):compile(s)
    def test_missing_rationale_or_permissive_tolerance_blocks(self):
        s=copy.deepcopy(MATCH);s['floors'][0]['height_ft']['rationale']=''
        with self.assertRaises(ValueError):compile(s)
        s=copy.deepcopy(MATCH);s['reconciliation']['absolute_tolerance_sf']=2000
        with self.assertRaisesRegex(ValueError,'0–1 sf'):compile(s)
    def test_source_error_ambiguity_wrong_parcel_and_crs_block(self):
        mutations=[lambda d:d.update(error={'message':'bad'}),lambda d:d['features'].append(copy.deepcopy(d['features'][0])),lambda d:d['features'][0]['attributes'].update(BBL=2028560051),lambda d:d.update(spatialReference={'wkid':4326}),lambda d:d.update(exceededTransferLimit=True)]
        for mutate in mutations:
            with self.subTest(mutate=mutate),tempfile.TemporaryDirectory() as d:
                root=alter_source(Path(d)/'source',mutate)
                with self.assertRaises(ValueError):sources.verify(root)
    def test_holes_and_multipart_are_not_silently_discarded(self):
        with tempfile.TemporaryDirectory() as d:
            root=alter_source(Path(d)/'source',lambda v:v['features'][0]['geometry']['rings'].append([[1,1],[1,2],[2,2],[1,1]]))
            with self.assertRaisesRegex(ValueError,'holes/multipart'):compile(source=root)
    def test_mesh_signed_volume_matches_independent_floor_volume(self):
        ir=compile();vs=ir['mesh']['vertices'];volume=0
        for i,j,k in ir['mesh']['triangles']:
            a,b,c=vs[i],vs[j],vs[k]
            cross=[b[1]*c[2]-b[2]*c[1],b[2]*c[0]-b[0]*c[2],b[0]*c[1]-b[1]*c[0]]
            volume+=sum(a[q]*cross[q] for q in range(3))/6
        expected=7500*14+5*6500*10
        self.assertAlmostEqual(volume,expected,places=5)
    def test_complete_run_replays_identically_and_original_analysis_untouched(self):
        with tempfile.TemporaryDirectory() as d:
            a,b=Path(d)/'a',Path(d)/'b'
            engine.build(ANALYSIS,SOURCE,MATCH,a);engine.build(ANALYSIS,SOURCE,MATCH,b)
            self.assertEqual(engine.inventory(a),engine.inventory(b))
            self.assertEqual((a/'analysis-run/manifest.json').read_bytes(),(ANALYSIS/'manifest.json').read_bytes())
            engine.verify(a)
    def test_altered_scenario_even_with_rehashed_manifest_stales_outputs(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';engine.build(ANALYSIS,SOURCE,MATCH,root)
            s=load(root/'scenario.json');s['floors'][0]['height_ft']['value']=16;save(root/'scenario.json',s)
            with self.assertRaisesRegex(ValueError,'artifact hash'):engine.verify(root)
            m=load(root/'manifest.json');m['files']=engine.inventory(root);save(root/'manifest.json',m)
            with self.assertRaisesRegex(ValueError,'differs from retained'):engine.verify(root)
    def test_corrupt_mesh_and_overwriting_existing_runs_block(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'run';engine.build(ANALYSIS,SOURCE,MATCH,root)
            with self.assertRaisesRegex(ValueError,'new empty'):engine.build(ANALYSIS,SOURCE,MATCH,root)
            (root/'massing.obj').write_text('v 0 0 0\n')
            with self.assertRaisesRegex(ValueError,'artifact hash'):engine.verify(root)
    def test_schema_and_json_unknown_fields(self):
        import jsonschema
        schema=load(ROOT/'housing_geometry/scenario.schema.json')
        for s in [MATCH,MISMATCH]:jsonschema.validate(s,schema)
        s=copy.deepcopy(MATCH);s['approved']=True
        with self.assertRaises(ValueError):compile(s)
        with self.assertRaises(jsonschema.ValidationError):jsonschema.validate(s,schema)
    def test_all_saved_geometry_examples(self):
        for name in ['allocation-mismatch','allocation-sensitivity']:
            engine.verify(ROOT/'examples/grounded-massing'/name)

if __name__=='__main__':unittest.main()

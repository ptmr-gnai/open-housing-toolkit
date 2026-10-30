"""Origin and assumption clarity must survive detached packets and hostile metadata."""
import copy
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from housing_workflow import context, contracts as c, engine, packet

EXAMPLE=engine.ROOT/'examples/parcel-investigation'


class PacketOpening(unittest.TestCase):
    def test_replay_does_not_query_and_discloses_dates_assumptions_and_unknowns(self):
        with tempfile.TemporaryDirectory() as d:
            run=Path(d)/'run'
            with patch.object(engine.router,'collect',side_effect=AssertionError('Network forbidden')):
                engine.replay(EXAMPLE,run)
            opening=(run/'packet.md').read_text().split('## Source coverage')[0]
            self.assertIn('Cached replay',opening)
            self.assertIn('2026-10-28',opening)
            self.assertIn('26v2',opening)
            self.assertIn('34.0 home-equivalents',opening)
            self.assertIn('#scenario-home_equivalents',opening)
            self.assertIn('#unknown-current_use',opening)
            self.assertNotIn('Queried four',opening)
            self.assertIn('href="execution.json"',(run/'packet.html').read_text())
            self.assertEqual(context.read(run).mode,context.EvidenceMode.REPLAY)

    def test_replay_cannot_be_relabelled_live_even_with_new_file_hashes(self):
        with tempfile.TemporaryDirectory() as d:
            run=Path(d)/'run';engine.replay(EXAMPLE,run)
            c.save(run/'execution.json',context.ExecutionContext(context.EvidenceMode.LIVE).to_dict())
            manifest=c.load(run/'manifest.json')
            manifest['files']['execution.json']=c.digest((run/'execution.json').read_bytes())
            c.save(run/'manifest.json',manifest)
            with self.assertRaisesRegex(ValueError,'relabeled'):
                engine.verify(run)

    def test_unrecorded_mode_is_not_inferred_from_recent_receipts(self):
        ir=c.load(EXAMPLE/'ir.json');receipts=c.load(EXAMPLE/'receipts.json')
        md,_,_=packet.projections(ir,receipts)
        self.assertIn('Collection mode was not recorded',md)
        self.assertNotIn('Queried four',md)

    def test_evidence_only_has_no_invented_area_result(self):
        with tempfile.TemporaryDirectory() as d:
            req=c.load(EXAMPLE/'request.json');req['scenario']=None
            run=Path(d)/'run';engine.replay(EXAMPLE,run,req)
            opening=(run/'packet.md').read_text().split('## Source coverage')[0]
            self.assertIn('No area assumptions were supplied',opening)
            self.assertNotIn('Conditional area-budget result:',opening)

    def test_failed_and_truncated_source_flags_are_visible_in_summary(self):
        receipts=copy.deepcopy(c.load(EXAMPLE/'receipts.json'))
        receipts[0]['status']='failed';receipts[1]['truncated']=True
        md,_,_=packet.projections(c.load(EXAMPLE/'ir.json'),receipts)
        opening=md.split('## Source coverage')[0]
        self.assertIn('failed: '+receipts[0]['id'],opening)
        self.assertIn('truncated: '+receipts[1]['id'],opening)

    def test_context_rejects_unknown_modes_and_impossible_source_bindings(self):
        for value in [
            {'version':'0.1.0','mode':'approved','source_manifest_sha256':None},
            {'version':'0.1.0','mode':'live_collection','source_manifest_sha256':'a'*64},
            {'version':'0.1.0','mode':'retained_snapshot_replay','source_manifest_sha256':None},
        ]:
            with self.assertRaises(ValueError):context.validate(value)

    def test_context_schema_matches_runtime_records(self):
        import jsonschema
        schema=c.load(engine.ROOT/'src/housing_workflow/execution.schema.json')
        for mode in context.EvidenceMode:
            value=context.ExecutionContext(mode,'a'*64 if mode in {context.EvidenceMode.REPLAY,context.EvidenceMode.ANALYSIS} else None).to_dict()
            jsonschema.validate(value,schema);context.validate(value)


if __name__=='__main__':unittest.main()

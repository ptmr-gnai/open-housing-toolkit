"""Counterexamples for budget propagation and independently frozen targets. MIT."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

CASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CASE))
spec = importlib.util.spec_from_file_location('stanyan_benchmark', CASE / 'benchmark.py')
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)


class BenchmarkTests(unittest.TestCase):
    def setUp(self):
        self.data = b.read(CASE / 'case-data.json')
        self.detail = b.read(CASE / 'operating-detail.json')
        self.contract = b.read(CASE / 'reference-contract.json')

    def change(self, name):
        return b.read(CASE / 'scenarios' / (name + '.json'))

    def test_independently_selected_report_values_and_rounding_bridges(self):
        b.validate_inputs(self.data, self.detail, self.contract)
        graph = b.model(self.data, self.detail)
        score = b.evaluate_reference(graph, self.contract)
        self.assertEqual(score['matched'], 15)
        self.assertEqual(graph.values['operations.egi_rounding_bridge'], -1)
        self.assertEqual(graph.values['operations.noi_rounding_bridge'], 1)
        self.assertEqual(graph.values['schedule.pro_rata_minus_reported'], 1)
        wrong_target = copy.deepcopy(self.contract)
        wrong_target['expected'][0]['value'] = '1.00'
        with self.assertRaisesRegex(ValueError, 'frozen reference'):
            b.assemble(self.data, self.detail, wrong_target, [])

    def test_operating_cost_shock_propagates_without_inventing_funding(self):
        base = b.model(self.data, self.detail)
        change = self.change('opex-plus-10')
        altered = b.model(self.data, self.detail, change)
        self.assertEqual(altered.values['operations.cashflow'], b.D('-31483.10'))
        self.assertEqual(altered.values['operations.income_needed_for_coverage'], b.D('188519.15'))
        self.assertEqual(altered.values['operations.losp'], base.values['operations.losp'])
        self.assertEqual(altered.values['capital.2023.total_uses'], base.values['capital.2023.total_uses'])
        self.assertEqual(b.decision(altered, self.data)['operating_screen'], 'below_selected_year_one_screen')
        affected = b.impact(base, altered, change)
        self.assertIn('operations.income_needed_for_coverage', affected['affected_nodes'])
        self.assertFalse(any(n.startswith('capital.') for n in affected['affected_nodes']))
        self.assertEqual(altered.values['operations.building_plus_separate_services'], b.D('3229071.10'))

    def test_losp_loss_does_not_rewrite_source_contract_schedule(self):
        altered = b.model(self.data, self.detail, self.change('without-losp'))
        self.assertEqual(altered.values['operations.cashflow'], -342236)
        self.assertEqual(altered.values['operations.income_needed_for_coverage'], b.D('499272.05'))
        self.assertEqual(altered.values['schedule.reported_sum'], 11720975)
        self.assertEqual(altered.values['capital.2023.total_sources'], 169152003)

    def test_capital_cost_shock_retains_rounding_gap_and_separate_operations(self):
        altered = b.model(self.data, self.detail, self.change('hard-cost-plus-10'))
        self.assertEqual(altered.values['capital.2023.additional_unallocated_capital'], b.D('12566466.50'))
        self.assertEqual(altered.values['capital.2023.unfunded_uses'], b.D('12566467.50'))
        self.assertEqual(altered.values['capital.2023.source_residual'], -1)
        self.assertEqual(altered.values['operations.noi'], 1272978)
        self.assertEqual(b.decision(altered, self.data)['capital_screen'], 'additional_funding_or_cost_revision_needed')

    def test_invalid_assumptions_and_duplicates_are_rejected(self):
        for value in ['NaN', 'Infinity', '-1', '11', None, 1.1]:
            change = self.change('opex-plus-10')
            change['value'] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                b.change_contract(change)
        change = self.change('opex-plus-10')
        change['automatically_adjust_subsidy'] = True
        with self.assertRaises(ValueError):
            b.change_contract(change)
        change = self.change('opex-plus-10')
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            b.assemble(self.data, self.detail, self.contract, [change, change])

    def test_services_cannot_be_counted_twice_in_expense_categories(self):
        self.detail['expense_categories_usd']['extra_psh_services'] = 395976
        with self.assertRaisesRegex(ValueError, 'do not reconcile'):
            b.validate_inputs(self.data, self.detail, self.contract)

    def test_dictionary_order_cannot_change_reports_or_dependency_trace(self):
        changes = [self.change('opex-plus-10')]
        first = b.assemble(self.data, self.detail, self.contract, changes)
        reordered = json.loads(json.dumps(self.data, sort_keys=True))
        other_detail = json.loads(json.dumps(self.detail, sort_keys=True))
        second = b.assemble(reordered, other_detail, self.contract, changes)
        self.assertEqual(b.rendered_files(first), b.rendered_files(second))

    def test_rehashed_fabricated_report_fails_recomputation(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder) / 'run'
            b.build(out, [self.change('opex-plus-10')])
            self.assertEqual(b.verify(out)['status'], 'passed')
            report = out / 'report.md'
            report.write_text(report.read_text().replace('Professional review: pending.', 'Professional review: approved.'))
            manifest = b.read(out / 'manifest.json')
            manifest['files']['report.md'] = b.evidence.sha(report)
            (out / 'manifest.json').write_text(b.canonical(manifest))
            with self.assertRaisesRegex(ValueError, 'recomputation'):
                b.verify(out)

    def test_completed_run_and_shipped_source_destination_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder) / 'run'
            b.build(out, [])
            with self.assertRaises(FileExistsError):
                b.build(out, [])
        with self.assertRaisesRegex(ValueError, 'read-only'):
            b.build(CASE / 'forbidden-output', [])


if __name__ == '__main__':
    unittest.main()

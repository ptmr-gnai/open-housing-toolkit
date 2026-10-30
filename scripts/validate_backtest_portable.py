"""Map the original root-cache paths while checking unchanged backtest records. MIT."""
import importlib.util,json
from pathlib import Path
from housing_common.local_outputs import ROOT
from housing_common.paths import historical_file


class RecordedRoot:
    def __truediv__(self,name):return historical_file(name)


spec=importlib.util.spec_from_file_location('recorded_backtest_validator',ROOT/'research/backtest-readiness/validate.py')
legacy=importlib.util.module_from_spec(spec);spec.loader.exec_module(legacy)
legacy.ROOT=RecordedRoot()
if __name__=='__main__':print(json.dumps(legacy.validate(),indent=2))

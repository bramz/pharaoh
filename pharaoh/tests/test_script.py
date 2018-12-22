from lib.reader import JSONReader
from engine.story import Script

class TestScript(object):
    def test_script(self):
        self.script =  Script('pharaoh/tests/fixtures/levels.json', JSONReader)
        assert self.script.data == {"levels": {"level0": "first level", "level1": "second level", "level2": "third level"}}

ts = TestScript()
ts.test_script()
from engine.story import Script, Story
from lib.reader import JSONReader


class TestStory(object):
    def test_get_levels(self):
        self.script = Script('pharaoh/tests/fixtures/levels.json', JSONReader)
        self.story = Story(self.script)
        self.levels = self.story.levels

        assert len(self.levels) == 3
        assert self.levels == {"level0": "first level", "level1": "second level", "level2": "third level"}


    def test_get_roles(self):
        self.script = Script('pharaoh/tests/fixtures/roles.json', JSONReader)
        self.story = Story(self.script)
        self.roles = self.story.levels['level0']['roles']

        assert len(self.roles) == 3
        assert self.roles == {"slave": "slave role", "laborer": "laborer role", "peasant": "peasant role"}

    def test_get_spawns(self):
        self.script = Script('pharaoh/tests/fixtures/spawns.json', JSONReader)
        self.story = Story(self.script)
        self.spawns = self.story.levels['level0']['roles']['slave']['spawns']


        assert len(self.spawns) == 3
        assert self.spawns == {"spawn0": "first spawn", "spawn1": "second spawn", "spawn2": "third spawn"}



tstory = TestStory()
tstory.test_get_levels()
tstory.test_get_roles()
tstory.test_get_spawns()
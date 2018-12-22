import random
from typing import List, Dict, Optional
from dataclasses import dataclass, field, InitVar
from lib.reader import Reader, JSONReader


@dataclass()
class Script:
    script: str
    reader: InitVar[Reader] = None
    data: Optional[Dict] = None
    def __post_init__(self, reader: Reader):
        if self.data is None and reader is not None:
            self.data = reader(self.script).data

class Story:
    script: Script
    def __init__(self, script: Script) -> None:
        self.script = script

    @property
    def levels(self) -> Dict:
        if isinstance(self.script.data, dict) \
            and self.script.data['levels'] is not None:
            return self.script.data['levels']
        else:
            return {}

    def get_roles(self, level: str) -> Dict:
        if isinstance(self.script.data, dict):
            return self.levels[level]['roles']
        else:
            return {}

    def get_spawns(self, level: str, role: str) -> Dict:
        if isinstance(self.script.data, dict):
            return self.get_roles(level)[role]['spawns']
        else:
            return {}



def spawn_option(story: Story, level: str, role: str, option: str) -> Dict:
    return story.get_spawns(level, role)[option]

def random_spawn(spawns: Dict) -> str:
    return random.choice([x for x in spawns if not x.startswith('@$\spawn') and not x.startswith('option')])


def random_option(spawns: Dict) -> str:
    return random.choice([x for x in spawns if not x.startswith('@$\option') and not x.startswith('spawn')])

def parse_options(options: Dict[str, List], opt: str) -> List:
    return options[opt]


""" Usage examples:
    script = Script('script.json', JSONReader)
    story  = Story(script)
    levels = story.levels
    roles = story.get_roles('level1')
    spawns = story.get_spawns('level1', 'craftsman')
    spawn_msg = spawn_option(story, 'level1', 'craftsman', random_spawn(spawns))
    options = spawn_option(story, 'level1', 'craftsman', random_option(spawns))

    print(levels, roles, spawns, options, spawn_msg, parse_options(options, '2'))
"""
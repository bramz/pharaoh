import json
import random
from typing import List, Dict


class Story:
    def __init__(self, data):
        self.data = data

    def get_levels(self) -> List:
        self.levels = list(self.data['levels'])

        return self.levels

    def get_roles(self, level: str) -> List:
        self.roles = list(self.data['levels'][level]['roles'])

        return self.roles


class Script:
    def __init__(self):
        self.script: str 

    def read_from_json(self, script: str) -> Story:
        self.script = script
        try:
            with open(self.script, 'r') as fh:
                data = json.load(fh)
                return Story(data)
        except IOError:
            return Story('')


def get_spawns(story: Story, level: str, role: str) -> List:
    spawns = story.data['levels'][level]['roles'][role]['spawns']
    return list(spawns)


def spawn_option(story: Story, level: str, role: str, option: str) -> List[Dict]:
    options = story.data['levels'][level]['roles'][role]['spawns'][option]
    return options


def random_spawn(spawns: Dict) -> str:
    return random.choice([x for x in spawns if not x.startswith('@$\spawn') and not x.startswith('option')])


def random_option(spawns: Dict) -> str:
    return random.choice([x for x in spawns if not x.startswith('@$\option') and not x.startswith('spawn')])


def parse_options(options: List[Dict], opt: str) -> str:
    return options[opt]

""" Usage examples """ 
"""
script = Script()
s = script.read_from_json('script.json')

levels = s.get_levels()
roles = s.get_roles('level1')
spawns = get_spawns(s, 'level1', 'craftsman')
spawn_msg = spawn_option(s, 'level1', 'craftsman', random_spawn(spawns))
options = spawn_option(s, 'level1', 'craftsman', random_option(spawns))

print(levels, roles, spawns, options, spawn_msg, parse_options(options, '2'))
"""

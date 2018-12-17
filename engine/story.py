import json
import random
from typing import List, Dict


class Story:
    def __init__(self, data):
        self.data = data

    def get_levels(self) -> List:
        self.levels = list(self.data['levels'])

        return [[y for y in x] for x in self.levels]

    def get_roles(self, level: str) -> List:
        self.roles = list(self.data['levels'][0][level][0]['roles'])

        return [[y for y in x] for x in self.roles]


class Script:
    def __init__(self):
        self.script: str 

    def read_story_script(self, script: str) -> Story:
        self.script = script
        try:
            with open(self.script, 'r') as fh:
                data = json.load(fh)
                return Story(data)
        except IOError:
            return Story('')


def get_spawns(story: Story, level: str, role: str) -> List:
    spawns = story.data['levels'][0][level][0]['roles'][0][role][0]['spawns']
    return list([[y for y in x] for x in spawns])


def spawn_option(story: Story, level: str, role: str, option: str) -> List[Dict]:
    options = story.data['levels'][0][level][0]['roles'][0][role][0]['spawns'][0][option]
    return options


def random_spawn(spawns: List) -> str:
    return random.choice([x for x in spawns[0] if not x.startswith('@$\spawn') and not x.startswith('option')])


def random_option(spawns: List) -> str:
    return random.choice([x for x in spawns[0] if not x.startswith('@$\option') and not x.startswith('spawn')])


def parse_options(options: List[Dict], opt: str) -> str:
    return options[0][opt]

""" Usage examples """ 
"""
script = Script()
s = script.read_story_script('script.json')

levels = s.get_levels()
roles = s.get_roles('level0')
spawns = get_spawns(s, 'level0', 'slave')
spawn_msg = spawn_option(s, 'level0', 'slave', random_spawn(spawns))
options = spawn_option(s, 'level0', 'slave', random_option(spawns))

print(levels, roles, spawns, options, spawn_msg, parse_options(options, '2'))
"""


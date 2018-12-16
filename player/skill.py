from dataclasses import dataclass
from collections import namedtuple


@dataclass
class Skill:
    abilities = namedtuple('Skillname', 'list of abilities')


@dataclass
class Carpentry(Skill):
    abilities = namedtuple('Carpentry', 'hammer cut measure build')


@dataclass
class Literature(Skill):
    abilities = namedtuple('Literature', 'reading writing vocabulary')


@dataclass
class Power(Skill):
    abilities = namedtuple('Power', 'telepathy flight magic invincibility')


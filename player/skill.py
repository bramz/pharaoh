from dataclasses import dataclass
from typing import NamedTuple


@dataclass
class Skill:
    abilities: NamedTuple


@dataclass
class Carpentry(Skill):
    abilities = ['hammer', 'cut', 'measure', 'build']


@dataclass
class Literature(Skill):
    abilities = ['reading', 'writing', 'vocabulary']


@dataclass
class Power(Skill):
    abilities = ['telepathy', 'flight', 'magic', 'invincibility']


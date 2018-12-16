from dataclasses import dataclass
from typing import List
from collection import namedtuple

skill_types = namedtuple('skill_types', 'carpentry literature power')

@dataclass(frozen=True)
class Skill:
    abilities = List[str]


@dataclass(frozen=True)
class Carpentry(Skill):
    abilities = ['hammer', 'cut', 'measure', 'build']


@dataclass(frozen=True)
class Literature(Skill):
    abilities = ['reading', 'writing', 'vocabulary']


@dataclass(frozen=True)
class Power(Skill):
    abilities = ['telepathy', 'flight', 'magic', 'invincibility']


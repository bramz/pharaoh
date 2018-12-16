import math
from dataclasses import dataclass
from typing import Dict
from player import skill_types


@dataclass(frozen=True)
class Level:
    experience: Dict[skill_types, int]

    def quantify_level(self, score: int):
        for k in self.experience:
            self.experience[k] = math.floor(self.experience[k] + pow(score-1, 2) * 3)



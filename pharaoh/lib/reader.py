import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional

""" Reader implementations
"""

@dataclass
class Reader():
    data: Dict = field(default_factory=dict)


@dataclass
class JSONReader(Reader):
    file: str
    data: Dict = field(init=False, repr=False)
    def __post_init__(self):
        with open(self.file, 'r') as f:
            self.data = dict(json.load(f))

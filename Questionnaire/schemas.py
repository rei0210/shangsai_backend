from dataclasses import dataclass
from typing import List

@dataclass
class Choice:
    rank:str
    content: str
    need_filled:bool

@dataclass
class Question:
    question_text: str
    choices: List[Choice]
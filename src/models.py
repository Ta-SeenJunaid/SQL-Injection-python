import random
from dataclasses import dataclass

@dataclass
class Message:
    msg_id: int
    user_id: int
    msg: str



from typing import Tuple, Any

from config import n_tiles


class ActionSpace:
    n: int

    def __init__(self):
        self.n = n_tiles


class Environment:
    action_space: ActionSpace

    def __init__(self):
        self.action_space = ActionSpace()

    def step(self, action: Any) -> Tuple[Any, float, bool, bool, dict]:
        raise NotImplemented

    def reset(self) -> Tuple[Any, dict]:
        raise NotImplemented

    def render(self):
        raise NotImplemented

from typing import Tuple

from config import green, red, gray


class Square:
    color: Tuple
    value: int

    def __init__(self, value: int):
        self.value = value
        self.color = self._get_color()

    def draw(self):
        pass

    def _get_color(self):
        if self.value > 0:
            return green
        elif self.value < 0:
            return red
        return gray

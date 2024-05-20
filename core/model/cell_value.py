from enum import Enum


class CellValue(Enum):
    EXPLOSION = -4
    MINE = -3
    FLAG = -2
    UNTOUCHED = -1
    TOUCHED = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8

    @classmethod
    def from_number(cls, value: int):
        if value >= 0 and value <= 9:
            return cls(value)
        else:
            raise ValueError(f"No CellValue found for value {value}")

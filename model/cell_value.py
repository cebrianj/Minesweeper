from enum import Enum


class CellValue(Enum):
    MINE = " 💣 "
    FLAG = " 🚩 "
    UNTOUCHED = " 🧱 "
    TOUCHED = " ⬜ "
    ONE = "  1 "
    TWO = "  2 "
    THREE = "  3 "
    FOUR = "  4 "
    FIVE = "  5 "
    SIX = "  6 "
    SEVEN = "  7 "
    EIGHT = "  8 "

    @classmethod
    def from_numerical_value(cls, value: int):
        if value == 1:
            return cls.ONE
        elif value == 2:
            return cls.TWO
        elif value == 3:
            return cls.THREE
        elif value == 4:
            return cls.FOUR
        elif value == 5:
            return cls.FIVE
        elif value == 6:
            return cls.SIX
        elif value == 7:
            return cls.SEVEN
        elif value == 8:
            return cls.EIGHT
        else:
            raise ValueError(f"No CellValue found for value {value}")

    def is_numerical(self):
        return self.value.strip().isdigit()

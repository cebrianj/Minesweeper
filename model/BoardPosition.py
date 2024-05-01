from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class BoardPosition:
    row_idx: int
    col_idx: int

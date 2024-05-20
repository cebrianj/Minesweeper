from typing import Iterable

from core.model.cell_value import CellValue


class BoardRepresentation:
    def __init__(
        self, board_data: Iterable[Iterable[CellValue | None]], size: int
    ) -> None:
        self.__board_data = board_data
        self.__board_size = size

    def get_rows(self) -> Iterable[Iterable[CellValue | None]]:
        return (row for row in self.__board_data)

    def get_columns(self) -> Iterable[Iterable[CellValue | None]]:
        size = len(self.__board_data)
        return ((row[col_idx] for row in self.__board_data) for col_idx in range(size))

    def get_size(self) -> int:
        return self.__board_size

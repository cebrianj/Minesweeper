from queue import SimpleQueue
from typing import Iterable
from model.board_position import BoardPosition
from model.board_representation import BoardRepresentation
from model.cell_value import CellValue
from model.range import Range


class Board:
    def __init__(self, board: Iterable[Iterable[CellValue]]) -> None:
        self.__board: list[list[CellValue]] = [row[:] for row in board]
        self.__size: int = len(self.__board)

    def get_representation(self) -> BoardRepresentation:
        return BoardRepresentation(Board.__hide_mines(row) for row in self.__board)

    def discover(self, position: BoardPosition) -> bool:
        if self.__get_cell_value(position) == CellValue.MINE:
            return True
        self.__discover_bfs(position)
        return False

    def __get_cell_value(self, position: BoardPosition) -> CellValue:
        return self.__get_cell_value_by_idx(position.row_idx, position.col_idx)

    def __discover_bfs(self, intial_position: BoardPosition) -> None:
        queue = SimpleQueue()
        visited = set()
        queue.put(intial_position)

        while not queue.empty():
            position: BoardPosition = queue.get()
            if position in visited:
                continue

            cellValue: CellValue = self.__get_cell_value(position)
            if cellValue == CellValue.MINE:
                continue

            nearby_mines_count: int = self.__get_nearby_mines_count(position)
            self.__set_cell_value(position, CellValue.from_number(nearby_mines_count))
            visited.add(position)

            if nearby_mines_count > 0:
                continue

            unvisisted_nearby_positions: Iterable[BoardPosition] = (
                pos
                for pos in self.__get_nearby_positions(position)
                if pos not in visited
            )

            for pos in unvisisted_nearby_positions:
                queue.put(pos)

    def __get_cell_value_by_idx(self, row_idx: int, col_idx: int) -> CellValue:
        return self.__board[row_idx][col_idx]

    def __set_cell_value(self, position: BoardPosition, content: CellValue):
        self.__set_cell_value_by_idx(position.row_idx, position.col_idx, content)

    def __set_cell_value_by_idx(self, row_idx: int, col_idx: int, content: CellValue):
        self.__board[row_idx][col_idx] = content

    def __get_nearby_mines_count(self, position: BoardPosition) -> int:
        nearby_positions: Iterable[BoardPosition] = self.__get_nearby_positions(
            position
        )
        return sum(
            (
                1
                for position in nearby_positions
                if self.__get_cell_value(position) == CellValue.MINE
            ),
            start=0,
        )

    def __get_nearby_positions(
        self, initial_position: BoardPosition
    ) -> Iterable[BoardPosition]:
        nearby_cols_range: Range = Range(
            start=max(initial_position.col_idx - 1, 0),
            end=min(initial_position.col_idx + 1, self.__size - 1),
        )
        nearby_rows_range: Range = Range(
            start=max(initial_position.row_idx - 1, 0),
            end=min(initial_position.row_idx + 1, self.__size - 1),
        )
        for row_idx in range(nearby_rows_range.start, nearby_rows_range.end + 1, 1):
            for col_idx in range(nearby_cols_range.start, nearby_cols_range.end + 1, 1):
                position = BoardPosition(row_idx, col_idx)
                if position == initial_position:
                    pass
                yield position

    @staticmethod
    def __hide_mines(cells: Iterable[CellValue]) -> Iterable[CellValue]:
        for cell in cells:
            # if cell == CellValue.MINE:
            #     yield CellValue.UNTOUCHED
            # else:
            yield cell

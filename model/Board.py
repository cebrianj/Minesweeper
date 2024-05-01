from collections import namedtuple
from dataclasses import dataclass
from typing import Callable

from model.BoardPosition import *
from model.BoardRepresentation import BoardRepresentaiton


Range = namedtuple("Range", "start end")


class Board:
    __MINE = "*"

    def __init__(self, size: int, mines: int, generate_random: Callable[[], int]):
        if mines > (size**2) / 4:
            raise Exception(
                "The number of mines cannot exceed 25% of the total number of positions"
            )

        self.__size = size
        self.__generate_random = generate_random
        self.__board: list[list[str]] = self.__initialize_board(size, mines)

    def discover(self, position: BoardPosition) -> bool:
        if self.__get_position_content(position) == self.__MINE:
            return True
        self.__set_position_content(position, self.__nearby_mines_count(position))

    def get_current_representation(self) -> BoardRepresentaiton:
        return tuple(tuple(row) for row in self.__board)

    def __set_position_content(self, position: BoardPosition, content: str):
        self.__board[position.row_idx][position.col_idx] = content

    def __nearby_mines_count(self, position: BoardPosition) -> int:
        max_col_idx = self.__size - 1
        max_row_idx = self.__size - 1
        cols_idxs_range = Range(
            start=position.col_idx - 1 if position.col_idx > 0 else 0,
            end=position.col_idx + 1 if position.col_idx < max_col_idx else max_col_idx,
        )
        rows_idxs_range = Range(
            start=position.row_idx - 1 if position.row_idx > 0 else 0,
            end=position.row_idx + 1 if position.row_idx < max_row_idx else max_row_idx,
        )

        counter = 0
        for row_idx in range(rows_idxs_range.start, rows_idxs_range.end + 1, 1):
            for col_idx in range(cols_idxs_range.start, cols_idxs_range.end + 1, 1):
                counter += (
                    1
                    if self.__get_position_content(row_idx, col_idx) == self.__MINE
                    else ...
                )
        return counter

    def __get_position_content(self, position: BoardPosition) -> str | None:
        return self.__board[position.row_idx][position.col_idx]

    def __get_position_content(self, row_idx, col_idx) -> str | None:
        return self.__board[row_idx][col_idx]

    def __initialize_board(self, size: int, mines: int):
        board = [[" "] * size for i in range(size)]
        minesPositions: set[BoardPosition] = self.__generate_random_mines_positions(
            size, mines
        )
        while len(minesPositions) < mines:
            minesPositions.update(self.__generate_random_mines_positions(size, mines))

        for minePosition in minesPositions:
            board[minePosition.row_idx][minePosition.col_idx] = self.__MINE
        return board

    def __generate_random_mines_positions(
        self, size: int, mines: int
    ) -> set[BoardPosition]:
        return {self.__generate_random_position(size) for i in range(mines)}

    def __generate_random_position(self, size: int) -> BoardPosition:
        return BoardPosition(
            row_idx=self.__generate_random() % size,
            col_idx=self.__generate_random() % size,
        )

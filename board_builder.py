import random
from model.cell_value import *
from model.board import Board

MAX_SIZE = 128


class BoardBuilder:
    def __init__(self) -> None:
        self.__board: list[list[str]] = None

    def build(self) -> Board:
        return Board(self.__board)

    def reset(self) -> "BoardBuilder":
        self.__board: list[list[str]] = None
        return self

    def set_size(self, size: int) -> "BoardBuilder":
        if size > MAX_SIZE:
            raise Exception(f"Size must be lower than {MAX_SIZE}")

        self.__board = [[CellValue.UNTOUCHED] * size for i in range(size)]
        return self

    def set_mines(self, mines: int) -> "BoardBuilder":
        if self.__board is None:
            raise Exception("Size must be set before mines")

        size = len(self.__board)
        if mines > (size**2) / 4:
            raise Exception(
                "The number of mines cannot exceed 25% of the total number of positions"
            )

        BoardBuilder.__set_mines_in_board(self.__board, mines)
        return self

    @staticmethod
    def __set_mines_in_board(board: list[list[str]], mines: int) -> None:
        size = len(board)
        flatten_mines_positions = random.sample(range(0, (size**2)), mines)
        for flatten_position in flatten_mines_positions:
            row_idx = flatten_position // size
            col_idx = flatten_position % size
            board[row_idx][col_idx] = CellValue.MINE

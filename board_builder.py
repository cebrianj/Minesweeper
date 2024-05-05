import random
from model.cell_value import *
from model.board import Board

MAX_SIZE = 128


class BoardBuilder:
    def __init__(self) -> None:
        self.__board: list[list[CellValue]] = None
        self.__size: int = None
        self.__mines: int = None

    def reset(self) -> "BoardBuilder":
        self.__board: list[list[CellValue]] = None
        self.__size: int = None
        self.__mines: int = None
        return self

    def set_size(self, size: int) -> "BoardBuilder":
        self.__size = size
        return self

    def set_mines(self, mines: int) -> "BoardBuilder":
        self.__mines = mines
        return self

    def build(self) -> Board:
        self.__board = BoardBuilder.__build_empty_board(self.__size)
        BoardBuilder.__place_mines_in_board(self.__board, self.__mines)
        return Board(self.__board)

    @staticmethod
    def __build_empty_board(size: int) -> list[list[CellValue]]:
        if size > MAX_SIZE:
            raise Exception(f"Size must be lower than {MAX_SIZE}")

        return [[CellValue.UNTOUCHED] * size for i in range(size)]

    @staticmethod
    def __place_mines_in_board(board: list[list[CellValue]], mines: int) -> None:
        if board is None:
            raise Exception("Size must be set before mines")

        size = len(board)
        if mines > (size**2) / 4:
            raise Exception(
                "The number of mines cannot exceed 25% of the total number of positions"
            )

        size = len(board)
        flatten_mines_positions = random.sample(range(0, (size**2)), mines)
        for flatten_position in flatten_mines_positions:
            row_idx = flatten_position // size
            col_idx = flatten_position % size
            board[row_idx][col_idx] = CellValue.MINE

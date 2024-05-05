from board_builder import BoardBuilder
from board_drawer import BoardDrawer
from model.board_position import BoardPosition


BOARD_SIZE = 10
MINES = 25


board = BoardBuilder().set_size(BOARD_SIZE).set_mines(MINES).build()
while True:
    BoardDrawer.draw(board)
    row_idx = int(input("row_idx:"))
    col_idx = int(input("col_idx:"))
    board.discover(BoardPosition(row_idx, col_idx))

import random
from model.Board import Board


BOARD_SIZE = 20
MINES = 10
board = Board(BOARD_SIZE,MINES,lambda: random.randint(0, BOARD_SIZE))
for i in board.get_current_representation():
    print(i)
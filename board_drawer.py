from model.board import Board
from model.cell_value import CellValue


class BoardDrawer:
    _CellValue_SymbolMap = {
        -3: " 💣 ",
        -2: " 🚩 ",
        -1: " 🧱 ",
        0: " ⬜ ",
        1: "  1 ",
        2: "  2 ",
        3: "  3 ",
        4: "  4 ",
        5: "  5 ",
        6: "  6 ",
        7: "  7 ",
        8: "  8 ",
    }

    @staticmethod
    def draw(board: Board) -> None:
        for row in board.get_representation().get_rows():
            print(
                "".join(
                    (
                        BoardDrawer._CellValue_SymbolMap[cellValue.value]
                        for cellValue in row
                    )
                )
            )

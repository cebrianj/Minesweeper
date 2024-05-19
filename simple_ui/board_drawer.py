from model.board import Board
from model.board_representation import BoardRepresentation
from model.cell_value import CellValue


class BoardDrawer:
    _CellValue_SymbolMap = {
        -4: "💥",
        -3: "💣",
        -2: "🚩",
        -1: "🧱",
        0: "🔲",
        1: " 1",
        2: " 2",
        3: " 3",
        4: " 4",
        5: " 5",
        6: " 6",
        7: " 7",
        8: " 8",
    }

    @staticmethod
    def draw(board_representation: BoardRepresentation) -> None:
        board_size = board_representation.get_size()

        # Calcula el ancho máximo para los índices y las celdas
        index_width = len(str(board_size - 1))
        cell_width = max(index_width, 4)  # Ajusta según el ancho de los símbolos

        # Genera la cabecera de la tabla con los índices de las columnas
        header = (
            f"|{"--".zfill(2):^{cell_width}}|"
            + "|".join(
                f"{str(idx).zfill(2):^{cell_width}}" for idx in range(board_size)
            )
            + f"|{"--".zfill(2):^{cell_width}}|"
        )

        separator = (
            "+" + "+".join("-" * cell_width for _ in range(board_size + 2)) + "+"
        )

        print(separator)
        print(header)
        print(separator)

        for row_idx, row in enumerate(board_representation.get_rows()):
            row_str = " | ".join(
                BoardDrawer._CellValue_SymbolMap[cell_value.value] for cell_value in row
            )
            row_index_str = f"{str(row_idx).zfill(2):^{cell_width}}"
            print(f"|{row_index_str}| {row_str} |{row_index_str}|")
            print(separator)

        print(header)
        print(separator)

from itertools import chain
from typing import Callable
from textual.widgets import Static, Button
from textual.app import ComposeResult

from core.model.board_position import BoardPosition
from core.model.board_representation import BoardRepresentation


class Board(Static):

    CELLVALUE_SYMBOLMAP = {
        -4: "💥",
        -3: "💣",
        -2: "🚩",
        -1: "🧱",
        0: "🔲",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
    }

    def initialize(
        self,
        board_representation: BoardRepresentation,
        on_cell_click: Callable[[BoardPosition], None],
    ) -> None:
        self._on_cell_click: Callable[[BoardPosition], None] = on_cell_click

        self.styles.set_rule("grid_size_rows", board_representation.get_size())
        self.styles.set_rule("grid_size_columns", board_representation.get_size())
        self.__buttons = [
            [
                (
                    Button(
                        self.CELLVALUE_SYMBOLMAP[cell.value],
                        classes="cell",
                        id=self.__generate_button_id(row_idx, col_idx),
                    )
                )
                for col_idx, cell in enumerate(row)
            ]
            for row_idx, row in enumerate(board_representation.get_rows())
        ]

    def compose(self) -> ComposeResult:
        return chain.from_iterable(self.__buttons)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        position = self.__get_board_position_from_id(button_id)
        self._on_cell_click(position)

    def update_view(self, board_representation: BoardRepresentation):
        for row_idx, row in enumerate(board_representation.get_rows()):
            for col_idx, cell in enumerate(row):
                button = self.__buttons[row_idx][col_idx]
                button.label = self.CELLVALUE_SYMBOLMAP[cell.value]
                button.height = 1
                button.refresh()

    def disable_interaction(self) -> None:
        for buttons_row in self.__buttons:
            for button in buttons_row:
                button.disabled = True

    def __generate_button_id(self, row_idx: int, col_idx: int) -> str:
        return f"_{row_idx}_{col_idx}"

    def __get_board_position_from_id(self, button_id: str) -> BoardPosition:
        _, row_idx, col_idx = button_id.split("_")
        return BoardPosition(int(row_idx), int(col_idx))

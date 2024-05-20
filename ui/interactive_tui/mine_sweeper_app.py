from typing import Callable
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

from ui.interactive_tui.board import Board
from ui.interactive_tui.information_panel import InformationPanel
from ui.model.execution_result import ExecutionResult
from core.model.board_position import BoardPosition
from core.model.board_representation import BoardRepresentation
from core.model.game_status import GameStatus


class MineSweeperApp(App):
    BINDINGS = [
        ("d", "toggle_dark()", "Toggle dark mode"),
        ("e", "exit()", "Exit"),
        ("r", "restart()", "Restart"),
    ]
    CSS_PATH = "styles.tcss"

    def initialize(
        self,
        discover_position: Callable[[BoardPosition], bool],
        get_board_representation: Callable[[None], BoardRepresentation],
        check_game_status: Callable[[None], GameStatus],
    ) -> "MineSweeperApp":
        self.discover_position = discover_position
        self.get_board_representation = get_board_representation
        self.check_game_status = check_game_status
        self.board = Board()
        self.board.initialize(self.get_board_representation(), self.on_cell_click)

        self.information_panel = InformationPanel()
        self.information_panel.initialize(self.action_restart)

        return self

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield self.information_panel
        yield self.board

    def on_mount(self) -> None:
        self.title = "Interactive MineSweeper"

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def action_exit(self) -> None:
        self.exit(result=ExecutionResult.OK)

    def action_restart(self) -> None:
        self.exit(result=ExecutionResult.RESTART)

    def on_cell_click(self, position: BoardPosition) -> None:
        self.discover_position(position)
        self.board.update_view(self.get_board_representation())
        game_status = self.check_game_status()
        if game_status != GameStatus.ONGOING:
            self.board.disable_interaction()
            self.information_panel.stop_timer()

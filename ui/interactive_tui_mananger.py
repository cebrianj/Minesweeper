from typing import Callable
from ui.interactive_tui.mine_sweeper_app import MineSweeperApp
from ui.model.execution_result import ExecutionResult
from core.model.board_position import BoardPosition
from core.model.board_representation import BoardRepresentation
from core.model.game_status import GameStatus
from ui.ui_manager import UIManager


class InteractiveTUIManager(UIManager):
    def __init__(
        self,
        discover_position: Callable[[BoardPosition], bool],
        get_board_representation: Callable[[None], BoardRepresentation],
        check_game_status: Callable[[None], GameStatus],
    ):
        self.discover_position = discover_position
        self.get_board_representation = get_board_representation
        self.check_game_status = check_game_status
        super().__init__(discover_position, get_board_representation, check_game_status)

    def run(self) -> ExecutionResult:
        return (
            MineSweeperApp()
            .initialize(
                self.discover_position,
                self.get_board_representation,
                self.check_game_status,
            )
            .run()
        )

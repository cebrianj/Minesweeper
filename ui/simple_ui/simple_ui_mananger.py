from typing import Callable
from ui.model.execution_result import ExecutionResult
from core.model.board_position import BoardPosition
from core.model.board_representation import BoardRepresentation
from core.model.game_status import GameStatus
from ui.simple_ui.board_drawer import BoardDrawer
from ui.ui_manager import UIManager
import common.utils as utils


class SimpleUIManager(UIManager):
    def __init__(
        self,
        discover_position: Callable[[BoardPosition], bool],
        get_board_representation: Callable[[None], BoardRepresentation],
        check_game_status: Callable[[None], GameStatus],
    ):
        self.discover_position = discover_position
        self.get_board_representation = get_board_representation
        self.check_game_status = check_game_status

        self.board_size = self.get_board_representation().get_size()

        super().__init__(discover_position, get_board_representation, check_game_status)

    def run(self) -> None:
        self.__print_board()
        while True:
            board_position = self.__ask_user_board_position()
            self.discover_position(board_position)
            self.__print_board()
            game_status = self.check_game_status()
            if game_status != GameStatus.ONGOING:
                break

        if self.__ask_user_if_restart():
            return ExecutionResult.RESTART
        return ExecutionResult.OK

    def __print_board(self) -> None:
        utils.clear_console()
        BoardDrawer.draw(self.get_board_representation())

    def __ask_user_board_position(self) -> BoardPosition:
        min_index = 0
        max_index = self.board_size - 1
        row_idx = utils.get_int_input(
            f"Select row index [{min_index}-{max_index}]: ", None, min_index, max_index
        )
        col_idx = utils.get_int_input(
            f"Select column index [{min_index}-{max_index}]: ",
            None,
            min_index,
            max_index,
        )
        return BoardPosition(row_idx, col_idx)

    def __ask_user_if_restart(self) -> bool:
        user_input = utils.get_int_input(
            f"Would you like to play again? [0 = false, 1 = true] (true): ",
            default=1,
            min_value=0,
            max_value=1,
        )

        return user_input == 1

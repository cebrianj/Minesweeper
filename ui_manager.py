import abc
from typing import Callable

from interactive_tui.execution_result import ExecutionResult
from model.board_position import BoardPosition
from model.board_representation import BoardRepresentation
from model.game_status import GameStatus


class UIManager(abc.ABC):
    @abc.abstractmethod
    def __init__(
        self,
        discover_position: Callable[[BoardPosition], bool],
        get_board_representation: Callable[[None], BoardRepresentation],
        check_game_status: Callable[[None], GameStatus],
    ):
        pass

    @abc.abstractmethod
    def run() -> ExecutionResult:
        pass

import abc
from typing import Callable

from ui.model.execution_result import ExecutionResult
from core.model.board_position import BoardPosition
from core.model.board_representation import BoardRepresentation
from core.model.game_status import GameStatus


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

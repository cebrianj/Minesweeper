from dataclasses import dataclass
from typing import Type

from ui.simple_ui.simple_ui_mananger import SimpleUIManager
from ui.ui_manager import UIManager


@dataclass
class GameSettings:
    board_size: int = 10
    mines: int = 25
    ui_manager_class: Type[UIManager] = SimpleUIManager

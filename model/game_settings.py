from dataclasses import dataclass

from model.ui_type import UIType


@dataclass
class GameSettings:
    board_size: int = 10
    mines: int = 25
    ui_type: UIType = UIType.TUI

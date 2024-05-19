import consts
from interactive_tui_mananger import InteractiveTUIManager
from model.ui_type import UIType
from simple_ui.simple_ui_mananger import SimpleUIManager
import utils
from model.game_settings import GameSettings


class SimpleSettingsWizard:

    __UI_MANAGERS = {
        UIType.SIMPLE.value: SimpleUIManager,
        UIType.TUI.value: InteractiveTUIManager,
    }

    @staticmethod
    def run() -> GameSettings:
        utils.clear_console()
        settings = GameSettings()
        print(consts.TITLE)
        print(consts.SETTINGS_SUBTITLE)

        board_size = utils.get_int_input(
            f"- Set the size of the board [5-15] ({consts.DEFAULT_BOARD_SIZE}): ",
            consts.DEFAULT_BOARD_SIZE,
            5,
            15,
        )

        mines_percentage = utils.get_percentage_input(
            f"- Set mines percentage [1% - 25%] ({int(consts.DEFAULT_MINES_PERCENTAGE*100)}): ",
            consts.DEFAULT_MINES_PERCENTAGE,
            0.01,
            0.25,
        )

        interface_type = utils.get_int_input(
            f"- Set UI type [0 = TUI, 1 = Simple] ({consts.DEFAULT_USER_INTERFACE.name}): ",
            consts.DEFAULT_USER_INTERFACE.value,
            0,
            1,
        )

        settings.board_size = board_size
        settings.mines = max(int(mines_percentage * (board_size**2)), 1)
        settings.ui_manager_class = SimpleSettingsWizard.__UI_MANAGERS[interface_type]
        return settings

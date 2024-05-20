from core.board_builder import BoardBuilder

from ui.model.execution_result import ExecutionResult
from ui.simple_settings_wizard import SimpleSettingsWizard


def run_game():
    settings = SimpleSettingsWizard.run()
    while True:
        board = (
            BoardBuilder()
            .set_size(settings.board_size)
            .set_mines(settings.mines)
            .build()
        )
        app = settings.ui_manager_class(
            board.discover, board.get_representation, board.check_game_status
        )
        execution_result = app.run()
        if execution_result != ExecutionResult.RESTART:
            break


if __name__ == "__main__":
    run_game()

from board_builder import BoardBuilder

from interactive_tui_mananger import InteractiveTUIManager
from simple_settings_wizard import SimpleSettingsWizard


# while True:
#     BoardDrawer.draw(board)
#     row_idx = int(input("row_idx:"))
#     col_idx = int(input("col_idx:"))
#     board.discover(BoardPosition(row_idx, col_idx))


def start_game():
    settings = SimpleSettingsWizard.run()
    board = (
        BoardBuilder().set_size(settings.board_size).set_mines(settings.mines).build()
    )
    app = InteractiveTUIManager(
        board.discover, board.get_representation, board.check_game_status, start_game
    )
    app.run()


if __name__ == "__main__":
    start_game()

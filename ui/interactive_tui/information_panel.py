from typing import Callable
from textual.widgets import Static, Button
from textual.app import ComposeResult

from ui.interactive_tui.counter_display import CounterDisplay
from ui.interactive_tui.time_display import TimeDisplay

RESET_BTN_ID = "reset"


class InformationPanel(Static):
    counter_display: CounterDisplay = None
    time_display: TimeDisplay = None

    def initialize(self, on_restart_game: Callable[[None], None]):
        self.on_restart_game = on_restart_game

    def on_mount(self):
        self.time_display.start()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == RESET_BTN_ID:
            self.on_restart_game()

    def compose(self) -> ComposeResult:
        self.counter_display = CounterDisplay()
        self.time_display = TimeDisplay()
        yield self.counter_display
        yield Button("🙂", id=RESET_BTN_ID)
        yield self.time_display

    def set_counter(self, number: int):
        self.counter_display.set(number)

    def stop_timer(self):
        self.time_display.stop_timer()

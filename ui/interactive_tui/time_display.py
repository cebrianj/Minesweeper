from textual.reactive import reactive
from textual.widgets import Static


from time import monotonic


class TimeDisplay(Static):
    start_time = reactive(monotonic)
    time = reactive(0.0)
    total = reactive(0.0)

    def on_mount(self) -> None:
        self.update_timer = self.set_interval(1 / 60, self.update_time, pause=True)

    def update_time(self) -> None:
        self.time = self.total + (monotonic() - self.start_time)

    def watch_time(self, time: float) -> None:
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        self.update(f"{hours:02,.0f}:{minutes:02.0f}:{seconds:02.0f}")

    def start(self) -> None:
        self.start_time = monotonic()
        self.update_timer.resume()

    def reset(self):
        self.total = 0
        self.time = 0

    def stop_timer(self) -> None:
        self.update_timer.pause()

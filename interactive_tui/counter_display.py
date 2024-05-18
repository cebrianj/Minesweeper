from textual.widgets import Static


class CounterDisplay(Static):
    number: int = 0

    def on_mount(self) -> None:
        self.__update_view()

    def set(self, number: int) -> None:
        self.number = number
        self.__update_view()

    def increment(self) -> None:
        self.number += 1
        self.__update_view()

    def decrement(self) -> None:
        self.number -= 1
        self.__update_view()

    def __update_view(self) -> None:
        self.update(f"{self.number}")

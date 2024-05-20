import os


def clear_console() -> None:
    print(os.name)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def get_int_input(prompt, default, min_value, max_value) -> int:
    while True:
        try:
            user_input = input(prompt)
            value = int(user_input) if user_input != "" else default
            if value is not None and min_value <= value <= max_value:
                return value
            print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Please enter a valid number.")


def get_percentage_input(prompt, default, min_value, max_value) -> float:
    while True:
        try:
            user_input = input(prompt)
            value = float(user_input) if user_input != "" else (default * 100)
            value /= 100
            if min_value <= value <= max_value:
                return value
            print(
                f"Please enter a value between {min_value*100}% and {max_value*100}%."
            )
        except ValueError:
            print("Please enter a valid value.")

from enum import Enum


class ExecutionResult(Enum):
    OK = 0
    ERROR = 1
    RESTART = 2

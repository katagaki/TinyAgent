from typing import Any

from common.classes import Function


class JoinAsStringFunction(Function):
    def __init__(self):
        super().__init__(
            name="String Join",
            description="Joins two elements together into a string, separated by a delimiter",
            output="The final joined string"
        )

    def do(self, left: Any, right: Any, delimiter: str = " ") -> str:
        return f"{left}{delimiter}{right}"

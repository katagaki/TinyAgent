from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel


class Function(ABC, BaseModel):
    name: str
    description: str
    output: str

    def __init__(self, name: str, description: str, output: str):
        super().__init__(**{
            "name": name,
            "description": description,
            "output": output
        })

    def __str__(self):
        return f"""{self.__class__.__name__}
- Name: {self.name}
- Description: {self.description}
- Output: {self.output}"""

    @abstractmethod
    def do(self, **kwargs) -> Any:
        raise NotImplementedError

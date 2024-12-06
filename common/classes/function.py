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

    @abstractmethod
    def do(self, **kwargs) -> Any:
        raise NotImplementedError

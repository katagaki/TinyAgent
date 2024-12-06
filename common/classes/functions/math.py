from common.classes import Function


class AddFunction(Function):
    def __init__(self):
        super().__init__(
            name="Number Addition",
            description="Adds two numbers together",
            output="The sum of the two numbers"
        )

    def do(self, a: int, b: int) -> int:
        return a + b


class SubtractFunction(Function):
    def __init__(self):
        super().__init__(
            name="Number Subtraction",
            description="Subtracts one number from another",
            output="The difference between the numbers"
        )

    def do(self, a: int, b: int) -> int:
        return a - b


class MultiplyFunction(Function):
    def __init__(self):
        super().__init__(
            name="Number Multiplication",
            description="Multiplies one number with another",
            output="The product of the numbers"
        )

    def do(self, a: int, b: int) -> int:
        return a * b


class DivideFunction(Function):
    def __init__(self):
        super().__init__(
            name="Number Division",
            description="Divides one number by another",
            output="The quotient of the numbers"
        )

    def do(self, a: int, b: int) -> float:
        return a / b

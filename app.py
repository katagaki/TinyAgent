from common.classes import (
    AddFunction,
    Function,
    SubtractFunction,
    MultiplyFunction,
    DivideFunction,
    GetWebpageFunction,
    JoinAsStringFunction
)
from common.extractors import extract_variables, extract_tasks
from common.selectors import select_function, select_functions

functions = [
    AddFunction(),
    SubtractFunction(),
    MultiplyFunction(),
    DivideFunction(),
    GetWebpageFunction(),
    JoinAsStringFunction()
]


def execute_instruction(user_message: str):
    function: Function = select_function(user_message, functions)

    if function:
        print(function.__class__.__name__)
        variables = extract_variables(user_message, function)
        print(variables)
        result = function.do(**variables)
        print(result)
    else:
        print("No function available for this question.")


def execute_instructions(user_message: str):
    tasks: list[str] = extract_tasks(user_message, functions)
    task_functions: list[dict] = select_functions(tasks, functions)

    if task_functions:
        print(task_functions)
        previous_result = None
        for task_function in task_functions:
            task: str = task_function["task"]
            function: Function = task_function["function"]
            print(task, function.__class__.__name__)
            variables = extract_variables(task, function)
            print(variables)
            for key, value in variables.items():
                if value == "%%":
                    variables[key] = previous_result
            print(variables)
            result = function.do(**variables)
            print(result)
            previous_result = result

    else:
        print("No functions available for this question.")


if __name__ == "__main__":
    # my_question: str = "Add the numbers 500 and 876 together"
    # my_question: str = "999-438"
    # my_question: str = "Multiply 5 by 38"
    # my_question: str = "60 / 5"
    # my_question: str = "I want the contents of https://docs.python.org/3.11/library/re.html#re.match"
    # my_question: str = "Add 100 to 250, then divide by 2. After that, multiply by 3 and take away 500"
    # my_question: str = "Divide 100 by 2, then repeat ten times."
    # my_question: str = "Divide 999 by 438, and present the answer like 'Result: result'"
    my_question: str = """I want to calculate my finances by tallying up all the money I owe to my friends. Here's a breakdown in a table:

| Lender        | Amount Owed | Due Date    | Status       | Notes                    |
|---------------|-------------|-------------|--------------|--------------------------|
| John Smith    | $250        | 2024-12-15  | Pending      | Personal loan            |
| Sarah Brown   | $500        | 2024-12-30  | Overdue      | Medical expenses         |
| Credit Card X | $1,200      | 2025-01-10  | Pending      | Monthly payment due      |
| David Lee     | $100        | 2024-12-20  | Pending      | Borrowed for groceries   |
| Family Fund   | $300        | 2025-02-01  | Pending      | Support for project      |
| Bank Loan     | $2,500      | 2025-03-01  | Pending      | Home improvement loan    |

Assuming the bank loan is paid, sum the remaining items and tell me how much I owe.
"""

    execute_instructions(my_question)

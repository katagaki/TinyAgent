from inspect import signature

from common.classes import Function
from common.llms import invoke_llm


def extract_tasks(user_message: str, functions: list[Function]) -> list[str]:
    functions_list: str = ""
    for function in functions:
        functions_list += f"{function.__str__()}\n"

    selection: dict = invoke_llm(
        message=f"""Divide up the user's queries into smaller tasks if it requires more than one step to achieve its goal.
If the user's query does not need further dividing, simply return it as is in the list.
If a task relies on a previous tasks's result, use the value '%%' instead.

The tasks can only be performed with the following functions:

{functions_list}

Question:
{user_message}
""",
        should_return_json_keys=["queries"]
    )

    return selection.get("queries", [])


def extract_variables(user_message: str, function: Function) -> dict:
    function_signature = signature(function.do)

    variables: dict = invoke_llm(
        message=f"""Given a function, extract the variables that should be passed into the function from the user's query.
Follow the function's signature when returning the variables.

Function Signature:
def {function.__class__.__name__}{function_signature}

Question:
{user_message}
""",
        should_return_json_keys=["variables"]
    )

    return variables.get("variables", {})

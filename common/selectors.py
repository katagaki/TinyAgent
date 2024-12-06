from common.classes import Function
from common.llms import invoke_llm


def select_function(user_message: str, functions: list[Function]) -> Function | None:
    functions_list: str = ""
    for function in functions:
        functions_list += f"""{function.__class__.__name__}
- Name: {function.name}
- Description: {function.description}
- Output: {function.output}
"""

    selection: dict = invoke_llm(
        message=f"""Given a function list, determine which function should be performed from the user's query.

Functions Available:
{functions_list}

Question:
{user_message}
""",
        should_return_json_keys=["function", "functionName", "reason"]
    )

    selected_function: str = selection["function"]
    matched_functions = [function for function in functions if function.__class__.__name__ == selected_function]
    if len(matched_functions) == 1:
        return matched_functions[0]
    else:
        return None


def select_functions(tasks: list[str], functions: list[Function]) -> list[dict]:
    task_list: list[dict] = []
    for task in tasks:
        selected_function = select_function(user_message=task, functions=functions)
        if selected_function is not None:
            task_list.append({
                "task": task,
                "function": selected_function
            })

    return task_list

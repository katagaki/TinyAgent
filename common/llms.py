import json
import os
from json import JSONDecodeError
from re import Match, search, MULTILINE

from dotenv import load_dotenv
from openai.lib.azure import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-10-21"
)
default_deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
default_system_message = "You are an assistant who keeps things short and sweet. Answer all questions in a concise manner."
default_system_json_mode_message = ("You are an assistant who works within the confines of a networked system. "
                                    "Answer all questions by returning a JSON object with the following keys: `{}`. "
                                    "Where numbers are involved, only include the number as the value.")


def invoke_llm(message: str, should_return_json_keys: list[str] = None, retry_count: int = 3) -> str | dict | None:
    if retry_count == -1:
        return None

    if should_return_json_keys:
        system_message: str = default_system_json_mode_message.format(", ".join(should_return_json_keys))
    else:
        system_message: str = default_system_message

    response = client.chat.completions.create(
        model=default_deployment_name,
        messages=[
            {
                "role": "system",
                "content": system_message
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )
    if should_return_json_keys:
        json_matches: Match = search(r"\{[\s\S]*\}", response.choices[0].message.content, MULTILINE)
        if json_matches:
            try:
                json_object = json.loads(json_matches.group(0))
                return json_object
            except JSONDecodeError as _:
                pass
        new_retry_count = retry_count - 1
        return invoke_llm(message, should_return_json_keys, new_retry_count)

    else:
        return response.choices[0].message.content


if __name__ == "__main__":
    print(invoke_llm(
        "How many iPhone 4Ses can you fit in a conventional Cadillac?"
    ))
    print(invoke_llm(
        "How many iPhone 4Ses can you fit in a conventional Cadillac?",
        should_return_json_keys=["cadillacSize", "iphoneSize", "iphoneCount"]
    ))

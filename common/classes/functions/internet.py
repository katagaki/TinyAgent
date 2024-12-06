from requests import get

from common.classes import Function


class GetWebpageFunction(Function):
    def __init__(self):
        super().__init__(
            name="Webpage GET",
            description="Gets the HTML content at a given URL",
            output="The downloaded HTML content"
        )

    def do(self, url: str) -> str:
        response = get(url)
        response.raise_for_status()
        return response.text

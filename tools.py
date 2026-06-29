import subprocess
import requests


def wikipedia_search(query):
    """
    Search Wikipedia using the official REST API.
    """
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"

        response = requests.get(
            url,
            headers={
                "User-Agent": "MultiToolAgent/1.0"
            },
            timeout=10
        )

        if response.status_code == 404:
            return "No Wikipedia page found."

        if response.status_code != 200:
            return f"Wikipedia request failed (HTTP {response.status_code})"

        data = response.json()

        if "extract" in data:
            return data["extract"]

        return "No summary available."

    except Exception as e:
        return f"Wikipedia error: {e}"


def get_weather(city):
    """
    Dummy weather tool.
    """
    return f"Weather lookup for '{city}' is not implemented yet."


def run_command(command):
    """
    Execute a system command and return its output.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return result.stdout.strip()

        return result.stderr.strip()

    except Exception as e:
        return str(e)


available_tools = {
    "wikipedia_search": wikipedia_search,
    "get_weather": get_weather,
    "run_command": run_command,
}
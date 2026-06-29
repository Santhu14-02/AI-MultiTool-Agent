import io
from contextlib import redirect_stdout

from prompts import SYSTEM_PROMPT
from gemini import ask_gemini
from parser import parse_json
from tools import available_tools


def run_agent(query):
    messages = []

    messages.append(
        {
            "role": "user",
            "content": SYSTEM_PROMPT
        }
    )

    messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    for _ in range(6):

        response = ask_gemini(messages)

        print("\nRAW MODEL OUTPUT:\n")
        print(response)

        data = parse_json(response)

        step = data["step"]

        if step == "plan":

            print("\n🧠 PLAN:")
            print(data["content"])

            messages.append(
                {
                    "role": "model",
                    "content": response
                }
            )

            messages.append(
                {
                    "role": "user",
                    "content": "Continue to the next step."
                }
            )

            continue

        elif step == "action":

            tool = data["function"]
            tool_input = data["input"]

            print(f"\n🛠 Calling Tool: {tool}({tool_input})")

            if tool not in available_tools:
                observation = f"Tool '{tool}' not found."
            else:
                observation = available_tools[tool](tool_input)

            print("\n👀 OBSERVATION:")
            print(observation)

            messages.append(
                {
                    "role": "model",
                    "content": response
                }
            )

            messages.append(
                {
                    "role": "user",
                    "content": f"Observation: {observation}"
                }
            )

            continue

        elif step == "output":

            return data["content"]

    return "Agent stopped after maximum iterations."


# NEW FUNCTION FOR STREAMLIT
def run_agent_with_logs(query):

    output = io.StringIO()

    with redirect_stdout(output):
        answer = run_agent(query)

    return {
        "answer": answer,
        "logs": output.getvalue()
    }


if __name__ == "__main__":

    while True:

        query = input("\nAsk me anything (or type exit): ")

        if query.lower() == "exit":
            break

        answer = run_agent(query)

        print("\n🤖 FINAL ANSWER:\n")
        print(answer)
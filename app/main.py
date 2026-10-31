import argparse
import os
import sys

from openai import OpenAI

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL", default="https://openrouter.ai/api/v1")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-p", required=True)
    args = p.parse_args()

    if not API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY is not set")

    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    chat = client.chat.completions.create(
        model="anthropic/claude-haiku-4.5",
        messages=[{"role": "user", "content": args.p}],
        tools = [{
              "type": "function",
              "function": {
                "name": "Read",
                "description": "Read and return the contents of a file",
                "parameters": {
                  "type": "object",
                  "properties": {
                    "file_path": {
                      "type": "string",
                      "description": "The path to the file to read"
                    }
                  },
                  "required": ["file_path"]
                }
              }
            }],

    )
    if not chat.choices or len(chat.choices) == 0:
        raise RuntimeError("no choices in response")
    message = chat.choices[0].message

    # Kiểm tra xem LLM có yêu cầu gọi công cụ (tool_calls) hay không
    if message.tool_calls:
        for tool_call in message.tool_calls:
            print(f"Tool call: {tool_call.function.name}")
            print(f"Arguments: {tool_call.function.arguments}")
    elif message.content:
        print(message.content)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    # TODO: Uncomment the following line to pass the first stage
    print(chat.choices[0].message.content)


if __name__ == "__main__":
    main()

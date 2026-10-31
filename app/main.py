# import argparse
# import os
# import sys
#
# from openai import OpenAI
#
# API_KEY = os.getenv("OPENROUTER_API_KEY")
# BASE_URL = os.getenv("OPENROUTER_BASE_URL", default="https://openrouter.ai/api/v1")
#
#
# def main():
#     p = argparse.ArgumentParser()
#     p.add_argument("-p", required=True)
#     args = p.parse_args()
#
#     if not API_KEY:
#         raise RuntimeError("OPENROUTER_API_KEY is not set")
#
#     client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
#
#     chat = client.chat.completions.create(
#         model="anthropic/claude-haiku-4.5",
#         messages=[{"role": "user", "content": args.p}],
#     )
#
#     if not chat.choices or len(chat.choices) == 0:
#         raise RuntimeError("no choices in response")
#
#     # You can use print statements as follows for debugging, they'll be visible when running tests.
#     print("Logs from your program will appear here!", file=sys.stderr)
#
#     # TODO: Uncomment the following line to pass the first stage
#     # print(chat.choices[0].message.content)
#
#
# if __name__ == "__main__":
#     main()

import argparse
from openai import OpenAI

def main():
    # 1. Khởi tạo parser để đọc tham số -p từ dòng lệnh
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--prompt", type=str, required=True, help="Prompt for the LLM")
    args = parser.parse_args()

    # 2. Khởi tạo client kết nối tới LLM
    client = OpenAI()

    # 3. Gửi yêu cầu tới LLM
    response = client.chat.completions.create(
        model="anthropic/claude-haiku-4.5",  # Giữ nguyên model mặc định của bài tập
        messages=[
            {"role": "user", "content": args.prompt}
        ]
    )

    # 4. In kết quả trả về của LLM ra màn hình (BẮT BUỘC)
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
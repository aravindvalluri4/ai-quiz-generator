import json
import os
import re

from openai import OpenAI, OpenAIError


def read_quiz_schema() -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "quiz_schema.json")
    with open(file_path, "r") as file:
        return file.read()


def generate_quiz(topic: str, question_count: int) -> dict:
    api_key: str = os.getenv("API_KEY", "set_api_key")
    quiz_json_schema = read_quiz_schema()
    try:
        client = OpenAI(api_key=api_key)

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a quiz master"},
                {
                    "role": "user",
                    "content": f"create a quiz on {topic} {question_count} qustion 4 options each and answers, set the reply in json with schema {quiz_json_schema}",
                },
            ],
        )
    except OpenAIError as e:
        print("Please check settings")
        raise e

    if completion.choices[0].message.content:
        match = re.search(
            r"```json\n(.*?)\n```", completion.choices[0].message.content, re.DOTALL
        )

        if match:
            json_string = match.group(1)
            quiz_dict = json.loads(json_string)
            print(quiz_dict)
            return quiz_dict

    raise Exception("Failed, to get quiz from ai")

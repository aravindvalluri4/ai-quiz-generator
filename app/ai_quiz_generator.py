import json
import os
import re
from typing import Dict

from openai import OpenAI, OpenAIError


def read_quiz_schema(file_name: str = "quiz_schema.json") -> str:
    """Read and return the contents of the quiz schema file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)
    with open(file_path, "r") as file:
        return file.read()


def generate_quiz(topic: str, question_count: int) -> Dict:
    """Generate a quiz based on the topic and number of questions, and return it as a dictionary."""
    api_key = os.getenv("API_KEY", "set_api_key")
    quiz_schema = read_quiz_schema()

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a quiz master"},
                {
                    "role": "user",
                    "content": (
                        f"Create a quiz on '{topic}' with {question_count} questions, "
                        "4 options each and answers. Provide the reply in JSON format "
                        f"matching this schema: {quiz_schema}"
                    ),
                },
            ],
        )
    except OpenAIError as e:
        print("Error communicating with OpenAI API. Please check settings.")
        raise e

    response_content = response.choices[0].message.content
    if response_content:
        match = re.search(r"```json\n(.*?)\n```", response_content, re.DOTALL)
        if match:
            json_string = match.group(1)
            try:
                quiz_dict = json.loads(json_string)
                return quiz_dict
            except json.JSONDecodeError:
                print("Error decoding JSON response.")
                raise
    raise Exception("Failed to get quiz from AI.")

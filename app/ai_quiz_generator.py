import os

from openai import OpenAI, OpenAIError

from .quiz_model import Quiz


class FailedToGenerateQuiz(Exception):
    message = "Failed to generate quiz properly"


def generate_quiz(topic: str, question_count: int) -> Quiz:
    """Generate a quiz based on the topic and number of questions, and return it as a dictionary."""
    api_key = os.getenv("API_KEY", "set_api_key")

    try:
        client = OpenAI(api_key=api_key)
        response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a quiz master"},
                {
                    "role": "user",
                    "content": (
                        f"Create a quiz on '{topic}' with {question_count} questions, "
                        "4 options each and answers."
                    ),
                },
            ],
            response_format=Quiz,
        )
    except OpenAIError as e:
        print("Error communicating with OpenAI API. Please check settings.")
        raise e

    response_content = response.choices[0].message.parsed
    if response_content:
        return response_content
    raise FailedToGenerateQuiz()

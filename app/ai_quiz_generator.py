import os

from openai import OpenAI, OpenAIError

from .quiz_model import Quiz


def read_quiz_schema(file_name: str = "quiz_schema.json") -> str:
    """Read and return the contents of the quiz schema file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)
    with open(file_path, "r") as file:
        return file.read()


def generate_quiz(topic: str, question_count: int) -> dict:
    """Generate a quiz based on the topic and number of questions, and return it as a dictionary."""
    api_key = os.getenv("API_KEY", "set_api_key")
    quiz_schema = read_quiz_schema()

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
                        "4 options each and answers. Provide the reply in JSON format "
                        f"matching this schema: {quiz_schema}"
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
        return response_content.model_dump()
    raise Exception("Failed to generate quiz")

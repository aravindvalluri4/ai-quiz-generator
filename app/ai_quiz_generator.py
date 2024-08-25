from openai import OpenAI
import re
import json


quiz_json_schema = """
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "quiz": {
      "type": "object",
      "properties": {
        "questions": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "question": {
                "type": "string"
              },
              "options": {
                "type": "array",
                "items": {
                  "type": "string"
                },
                "minItems": 1
              },
              "answer": {
                "type": "string"
              }
            },
            "required": ["question", "options", "answer"],
            "additionalProperties": false
          }
        }
      },
      "required": ["questions"],
      "additionalProperties": false
    }
  },
  "required": ["quiz"],
  "additionalProperties": false
}
"""


def generate_quiz(topic, question_count):
    client = OpenAI()

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

    match = re.search(
        r"```json\n(.*?)\n```", completion.choices[0].message.content, re.DOTALL
    )

    if match:
        json_string = match.group(1)
        # Convert to dictionary
        quiz_dict = json.loads(json_string)
        print(quiz_dict)
        return quiz_dict
    else:
        raise Exception("Failed")

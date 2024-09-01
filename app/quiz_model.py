from pydantic import BaseModel


class Question(BaseModel):
    question: str
    options: list[str]
    answer: str


class Quiz(BaseModel):
    questions: list[Question]

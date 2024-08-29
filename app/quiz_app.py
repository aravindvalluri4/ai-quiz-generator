import tkinter as tk
from tkinter import messagebox
from typing import Any


class QuizApp:
    def __init__(self, questions: list[Any], topic: str) -> None:
        self.questions = questions
        self.current_question = 0
        self.answers = [None] * len(self.questions)
        self.score = 0

        self.root = tk.Tk()
        self.root.title(f"{topic} Quiz")
        self.display_question()
        self.create_navigation_buttons()

    def run(self) -> None:
        self.root.mainloop()

    def display_question(self) -> None:
        question_data = self.questions[self.current_question]
        question_text = question_data["question"]
        options = question_data["options"]

        # Clear previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Display question
        self.question_label = tk.Label(
            self.root, text=question_text, font=("Arial", 14)
        )
        self.question_label.pack(pady=20)

        # Variable to hold the selected answer
        self.selected_answer = tk.StringVar()
        self.selected_answer.set(None)  # type: ignore

        # Display options as radio buttons
        for option in options:
            rb = tk.Radiobutton(
                self.root,
                text=option,
                variable=self.selected_answer,
                value=option,
                font=("Arial", 12),
                anchor="w",
            )
            rb.pack(fill="x", padx=20)

        # Set the selected answer for this question if previously answered
        if self.answers[self.current_question]:
            self.selected_answer.set(self.answers[self.current_question])

    def create_navigation_buttons(self) -> None:
        # Previous Button
        if self.current_question > 0:
            prev_button = tk.Button(
                self.root, text="Previous", command=self.previous_question
            )
            prev_button.pack(side="left", padx=20, pady=20)

        # Submit Button
        if self.current_question == len(self.questions) - 1:
            submit_button = tk.Button(
                self.root, text="Submit", command=self.submit_quiz
            )
            submit_button.pack(side="right", padx=20, pady=20)
        else:
            next_button = tk.Button(self.root, text="Next", command=self.next_question)
            next_button.pack(side="right", padx=20, pady=20)

    def next_question(self) -> None:
        self.answers[self.current_question] = self.selected_answer.get()  # type: ignore
        self.current_question += 1
        self.display_question()
        self.create_navigation_buttons()

    def previous_question(self) -> None:
        self.current_question -= 1
        self.display_question()
        self.create_navigation_buttons()

    def submit_quiz(self) -> None:
        self.answers[self.current_question] = self.selected_answer.get()  # type: ignore
        self.evaluate_score()
        messagebox.showinfo(
            "Quiz Result", f"Your score is {self.score}/{len(self.questions)}"
        )
        self.root.destroy()

    def evaluate_score(self) -> None:
        for i, question in enumerate(self.questions):
            if self.answers[i] == question["answer"]:
                self.score += 1

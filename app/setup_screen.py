import tkinter as tk
from tkinter import messagebox

from .ai_quiz_generator import generate_quiz
from .quiz_app import QuizApp
from .quiz_model import Quiz


class SetupScreen(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Select Quiz Topic and Number of Questions")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self) -> None:
        # Topic Entry
        tk.Label(self, text="Enter Quiz Topic:", font=("Arial", 12)).pack(pady=10)
        self.topic_entry = tk.Entry(self, width=50)
        self.topic_entry.pack(pady=5)

        # Number of Questions
        tk.Label(self, text="Select Number of Questions:", font=("Arial", 12)).pack(
            pady=10
        )
        self.num_questions_var = tk.StringVar(value="3")
        num_questions_options = ["3", "5", "10"]
        self.num_questions_menu = tk.OptionMenu(
            self, self.num_questions_var, *num_questions_options
        )
        self.num_questions_menu.pack(pady=5)

        # Start Quiz Button
        tk.Button(self, text="Start Quiz", command=self.start_quiz).pack(pady=20)

    def start_quiz(self) -> None:
        topic = self.topic_entry.get().strip()
        num_questions = int(self.num_questions_var.get())

        if not topic:
            messagebox.showwarning("Invalid Input", "Please enter a topic.")
            return

        if num_questions < 1:
            messagebox.showwarning(
                "Invalid Input", "Number of questions must be at least 1."
            )
            return
        self.quiz_data = generate_quiz(topic, num_questions)

        self.destroy()

        QuizApp(
            self.quiz_data, topic
        ).run()  # Pass the selected questions to the QuizApp

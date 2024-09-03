# AI Quiz Generator

## Overview

AI Quiz Generator is a simple quiz application built using the Tkinter library for the graphical user interface (GUI). The app leverages the OpenAI API to generate quiz questions on a specific topic. Users can navigate through the questions, select their answers, and submit the quiz to see their score.

## Features

- **Create Quiz:** Users can choose a topic and the number of questions. The app generates the quiz by making a call to the OpenAI API.
- **Multiple-choice questions:** Users can choose from multiple options for each question.
- **Navigation buttons:** Users can navigate between questions using "Previous" and "Next" buttons.
- **Score calculation:** The app evaluates the user's answers and displays the final score upon submission.

## Installation

### Prerequisites

- Ensure you have Python installed on your machine.
- Create an OpenAI account and recharge credits.($5 should be enough)
- Generate an API key from OpenAI.

### Setup

1. Create a virtual environment:
   ```bash
   python -m virtualenv .venv
   pip install -r requirements.txt
   export API_KEY="generated_key_from_open_api_account"
   python main.py
   


# Quiz App

This is a simple quiz application written in Python. It loads questions from a JSON file, presents them to the user, and evaluates their answers. 

## Features

- Loads questions from a JSON file.
- Randomizes question order and answer choices.
- Allows the user to select their answer from multiple-choice options.
- Provides feedback on the correctness of the user's answer.
- Calculates the user's final score at the end of the quiz.

## How to Use

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/quiz-app.git
```

2. Navigate to the project directory:

```bash
cd quiz-app
```

3. Run the quiz application:

```bash
python quiz.py
```

4. Follow the on-screen instructions to answer the questions and complete the quiz.

## Requirements

- Python 3.x
- JSON file containing quiz questions and answers

## JSON File Format

The quiz questions and answers are stored in a JSON file. The format of each question object in the JSON file is as follows:

```json
{
  "question": "What is the capital of France?",
  "correct_answer": "Paris",
  "incorrect_answers": ["London", "Berlin", "Rome"]
}
```

Ensure that your JSON file follows this format.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

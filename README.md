# Quiz Game

This is a simple quiz game implemented in Python. The game allows players to answer a series of questions and keeps track of high scores. 
Players can also adjust the number of questions in the quiz and clear all scores.

## Features

- Play a quiz game with a customizable number of questions.
- Save and display high scores.
- Clear all scores.
- User-friendly main menu.

## Getting Started

These instructions will help you set up and run the quiz game on your local machine.

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/quiz-game.git
   cd quiz-game
   ```

2. Install any necessary dependencies (if there are any). In this example, we assume that there are no external dependencies beyond standard Python libraries.

### Usage

1. Ensure you have a `questions.json` file in the same directory as your script. This file should contain your quiz questions in JSON format.

   Example `questions.json`:

   ```json
   [
       {
           "question": "What is the capital of France?",
           "choices": ["Paris", "London", "Rome", "Berlin"],
           "answer": "Paris"
       },
       {
           "question": "What is 2 + 2?",
           "choices": ["3", "4", "5", "6"],
           "answer": "4"
       }
       // Add more questions as needed
   ]
   ```

2. Run the main script:

   ```bash
   python main.py
   ```

3. Follow the on-screen instructions to play the game, change settings, or clear scores.

## Main Functions

### `settings()`

Allows the user to set the number of questions for the quiz. Ensures that the input is a positive integer.

### `clear_scores_menu()`

Prompts the user to confirm whether they want to clear all scores. Clears scores if confirmed.

### `main_menu()`

Displays the main menu, where users can choose to play the game, change settings, clear scores, or exit the game.

### `if __name__ == "__main__":`

Entry point of the program. Calls the `main_menu()` function to start the game.

## File Structure

```
quiz-game/
│
├── main.py               # Main script to run the quiz game
├── quiz.py               # Module containing quiz-related functions
├── scores.py             # Module for handling scores
├── questions.json        # JSON file containing quiz questions
└── README.md             # This README file
```

## Acknowledgments

- Inspiration and guidance for this project were taken from various Python programming tutorials and resources.
- Special thanks to the contributors and maintainers of Python and its libraries.


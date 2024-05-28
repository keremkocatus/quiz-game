import json
import random

def load_questions_from_json(filename):
    with open(filename, 'r') as file:
        questions = json.load(file)
    return questions

def ask_question(question):
    print("\n" + question["question"])
    options = question["incorrect_answers"] + [question["correct_answer"]]
    random.shuffle(options)
    choices = ['A', 'B', 'C', 'D']
    for i, option in enumerate(options):
        print(f"{choices[i]}. {option}")

    while True:
        choice = input("Enter your answer (A, B, C, or D): ").strip().upper()
        if choice in ['A', 'B', 'C', 'D']:
            break
        else:
            print("Invalid input. Please enter A, B, C, or D.")
    user_choice = options[choices.index(choice)]
    return user_choice == question["correct_answer"], question["correct_answer"]

def quiz(questions):
    random.shuffle(questions)
    score = 0
    total_questions = 10
    for i, question in enumerate(questions[:total_questions], start=1):
        print(f"\nQuestion {i}/{total_questions}:")
        correct, correct_answer = ask_question(question)
        if correct:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}")
    print(f"\nYour final score is {score}/{total_questions}")

if __name__ == "__main__":
    questions = load_questions_from_json('questions.json')
    quiz(questions)

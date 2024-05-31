import random
import json
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def quiz(questions, total_questions, player_name):
    random.shuffle(questions)
    score = 0
    for i, question in enumerate(questions[:total_questions], start=1):
        print(f"\nQuestion {i}/{total_questions}:")
        correct, correct_answer = ask_question(question)
        if correct:
            print("\033[92mCorrect!\033[0m")
            score += 1
        else:
            print(f"\033[91mIncorrect! The correct answer is: {correct_answer}\033[0m")
        
        input("\nPress the enter to continue to the next question... ").strip()
        clear_screen()
    
    print(f"\nYour final score is {score}/{total_questions}")
    
    return score
import quiz
import scores

def settings():
    while True:
        try:
            total_questions = int(input("Enter the number of questions for the quiz: "))
            if total_questions > 0:
                return total_questions
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def clear_scores_menu():
    choice = input("Are you sure you want to clear all scores? (yes/no): ").strip().lower()
    if choice == 'yes':
        scores.clear_scores()
        print("Scores cleared successfully!")
    elif choice == 'no':
        print("Scores were not cleared.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

def main_menu():
    total_questions = 10
    questions = quiz.load_questions_from_json('questions.json')
    
    while True:
        quiz.clear_screen()
        high_scorer, high_correct, high_total = scores.get_high_score()
        if high_scorer:
            print(f"High Score: {high_correct}/{high_total} by {high_scorer}")
        else:
            print("No high scores yet.")
        print("\nMain Menu:")
        print("1. Play")
        print("2. Settings")
        print("3. Clear Scores")
        print("4. Exit")
        choice = input("Enter your choice (1, 2, 3, or 4): ").strip()
        
        if choice == '1':
            player_name = scores.get_player_name()
            while True:
                quiz.clear_screen()
                score = quiz.quiz(questions, total_questions, player_name)
                scores.save_score(player_name, score, total_questions)
                print("\n1. Play Again")
                print("2. Main Menu")
                print("3. Exit")
                post_quiz_choice = input("Enter your choice (1, 2, or 3): ").strip()
                
                while post_quiz_choice not in ['1', '2', '3']:
                    print("Invalid choice. Please enter 1, 2, or 3.")
                    post_quiz_choice = input("Enter your choice (1, 2, or 3): ").strip()
                
                if post_quiz_choice == '1':
                    break
                elif post_quiz_choice == '2':
                    break
                elif post_quiz_choice == '3':
                    print("Exiting the game. Goodbye!")
                    return
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
        elif choice == '2':
            total_questions = settings()
        elif choice == '3':
            clear_scores_menu()
        elif choice == '4':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main_menu()

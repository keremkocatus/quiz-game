import json

def get_player_name():
    return input("Enter your name: ").strip()

def load_scores(filename='scores.json'):
    try:
        with open(filename, 'r') as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = []
    return scores

def save_score(player_name, correct_answers, total_questions, filename='scores.json'):
    scores = load_scores(filename)
    scores.append({"name": player_name, "correct_answers": correct_answers, "total_questions": total_questions})
    with open(filename, 'w') as file:
        json.dump(scores, file)

def get_high_score(filename='scores.json'):
    scores = load_scores(filename)
    if scores:
        high_score = max(scores, key=lambda x: x['correct_answers'] / x['total_questions'] if x['total_questions'] > 0 else 0)
        return high_score['name'], high_score['correct_answers'], high_score['total_questions']
    return None, None, None

def clear_scores(filename='scores.json'):
    with open(filename, 'w') as file:
        file.write("[]")
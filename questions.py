import requests
import json
import html
import time

def fetch_questions_from_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch questions from {url}. Status code: {response.status_code}")
        return []
    data = response.json()
    if 'results' not in data:
        print(f"Unexpected response structure from {url}: {data}")
        return []
    questions = []
    for item in data['results']:
        question = {
            "question": html.unescape(item['question']),
            "correct_answer": html.unescape(item['correct_answer']),
            "incorrect_answers": [html.unescape(ans) for ans in item['incorrect_answers']]
        }
        questions.append(question)
    return questions

def fetch_questions(urls):
    all_questions = []
    for url in urls:
        questions = fetch_questions_from_url(url)
        if questions:
            all_questions.extend(questions)
        time.sleep(5)
    return all_questions

def save_questions_to_json(questions, filename):
    with open(filename, 'w') as file:
        json.dump(questions, file, indent=4)

if __name__ == "__main__":

    urls = [
        f"https://opentdb.com/api.php?amount=50&category={category_id}&difficulty=easy&type=multiple"
        for category_id in range(9, 33)
    ]
    
    questions = fetch_questions(urls)
    if questions:
        save_questions_to_json(questions, 'questions.json')
        print("Questions have been saved to questions.json")
    else:
        print("No questions were fetched.")

import requests

url = "https://tryvia.ptr.red/api.php?amount=20&difficulty=easy"

questions = requests.get(url).json()["results"]

questions = [{
    'question': question['question'],
    'answersIncorrect':','.join(question['incorrect_answers']),
    'answersCorrect': question['correct_answer']
} for question in questions]

try:
    for q in questions:
        requests.post('http://localhost:8000/question', json=q)
except Exception as e:
    print(e)
    
from fastapi import APIRouter
from model.quiz import Quiz

router = APIRouter()

@router.get('/questionOne/{question_one_id}')
def question_one(question_one:Quiz):
    answer = question_one
    return {answer}

@router.get('/questionTwo/{question_two_id}')
def question_two(question_two:Quiz):
    answer = question_two
    return {answer}
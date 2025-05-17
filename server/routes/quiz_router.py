from fastapi  import APIRouter
from models.quiz_model import QuizDTO
from controllers import quiz_controller
import asyncio

router = APIRouter()
quiz_controller = quiz_controller

@router.get('/quiz/{id}')
async def get_quiz(id: int):
    return await quiz_controller(id)

@router.post('/quiz')
async def create_quiz(quiz: QuizDTO):
    return await quiz_controller(quiz)
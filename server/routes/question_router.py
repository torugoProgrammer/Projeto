from fastapi import APIRouter
from models.question_model import QuestionDTO
from controllers.question_controller import QuestionController
import asyncio

router = APIRouter()
question_controller = QuestionController()

@router.get('/question/{id}')
async def get_question(id: int):
    return await question_controller.get_by_id(id)

@router.get('/question')
async def get_all_questions():
    return await question_controller.get_all()

@router.post('/question')
async def create_question(question: QuestionDTO):
    return await question_controller.create(question)

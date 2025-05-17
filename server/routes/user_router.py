from fastapi import APIRouter
from controllers.user_controller import UserController 
from models.user_model import UserDTO
import asyncio

router = APIRouter()
user_controller = UserController()

@router.get('/user/{id}')
async def get_user(id: int):
    return await user_controller.get_by_id(id)

@router.post('/user')
async def create_user(user: UserDTO):
    return await user_controller.create(user)
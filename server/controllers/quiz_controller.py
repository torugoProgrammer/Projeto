from models.quiz_model import Quiz, QuizDTO
from fastapi import HTTPException, Response
from prisma import Prisma

class QuizController:
    def __init__(self):
        self.db = Prisma()
    
    async def get_by_id(self, id: int) -> Quiz:
        await self.db.connect()
        
        try:
            result = await self.db.quiz.first(where={"id": id})    
            return result
        except Exception as e:
            await self.db.disconnect()
            raise e

    async def create(self, quiz: QuizDTO) -> Quiz:
        await self.db.connect()
        quiz = quiz.model_dump()
        try:
            result = self.db.quiz.create(data=quiz)
            return result
        except Exception as e:
            await self.db.disconnect()
            raise e
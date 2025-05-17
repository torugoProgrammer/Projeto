from models.question_model import Question, QuestionDTO
from prisma import Prisma
from fastapi import HTTPException, Response

class QuestionController:
    def __init__(self):
        self.db = Prisma()
        
    async def get_by_id(self, id: int) -> Question:
        await self.db.connect() 
          
        try:
            result = await self.db.question.find_first(where={"id": id})
            await self.db.disconnect()
            return result
        except Exception as e:
            await self.db.disconnect()
            raise e
    
    async def create(self, question: QuestionDTO) -> Question:
        await self.db.connect()
        question = question.model_dump()
        try:
            result = await self.db.question.create(data=question)
            await self.db.disconnect() 
            return result
        except Exception as e:
            await self.db.disconnect()
            print(e)
            raise e
    
    async def get_all(self) -> list[Question]:
        await self.db.connect()
        try:
            result = await self.db.question.find_many()
            return result
        
        except Exception as e:
            await self.db.disconnect()
            raise e
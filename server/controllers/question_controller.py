from models.question_model import Question, QuestionDTO
from prisma import Prisma
from fastapi import HTTPException, Response
import random

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
    
    async def take_random(self, count: int) -> list[Question]:
            await self.db.connect()
            result = None
            try:
                questions = await self.db.question.find_many()
                result = random.sample(questions, count)
                await self.db.disconnect()
                return result
            except Exception as e:
                await self.db.disconnect()
                raise e
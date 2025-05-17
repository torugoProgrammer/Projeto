from models.user_model import User, UserDTO
from fastapi import HTTPException, Response
from prisma import Prisma


class UserController:
    def __init__(self):
        self.db = Prisma()
    
    async def get_by_id(self, id: int) -> User:
        await self.db.connect()

        try:
            result = self.db.user.find_first(where={"id": id})
            return result
        except Exception as e:
            await self.db.disconnect()
            raise e

    async def create(self, user: UserDTO) -> User:
        await self.db.connect()
        user = user.model_dump()
        try:
            result = await self.db.user.create(data=user)
            return result
        except Exception as e:
            self.db.disconnect()
            raise e
                    
    
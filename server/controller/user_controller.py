import asyncio
from model.user import User
from sqlmodel import Session, select, col, delete, update

class UserController:
    async def get_user(self, id: int):
        with Session() as session:
            cmd = select(User).where(User.id == id)
        
            try:
                result = session.exec(cmd)
                return result.first()
            except Exception as e: 
                print(e)
                return {"message":404}
    # async def get_by_id():
    #     return None
    # async def delete_by_id():
    #     return None
    # async def update_by_id():
    #     return None
    
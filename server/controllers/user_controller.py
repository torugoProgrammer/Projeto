from models.user_model import User, UserDTO
from sqlmodel import Session, select
from fastapi import HTTPException, Response


class UserController:
    def get_by_id(self, id: int):
        with Session() as session:
            cmd = select(User).where(User.id == id)

            try:
                result = session.exec(cmd)
                return Response(result.first(), status_code=200)
            except Exception:
                raise HTTPException(status_code=404, detail="User not found") 

    def create(self, user: User):
        with Session() as session:
            try:
                session.add(user)
                session.commit()
                session.refresh(user)
                return Response(user, status_code=201)
            except Exception as e:
                print(e)
                raise HTTPException(status_code=404, detail='Not possible to create')
                    
    
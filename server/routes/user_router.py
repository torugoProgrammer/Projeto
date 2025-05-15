from fastapi import APIRouter
from controllers.user_controller import UserController 
from models.user_model import User

router = APIRouter()
user_controller = UserController()

@router.get('/user/{id}')
def get_user(id: int):
    return user_controller.get_by_id(id)

@router.post('/user')
def create_user(user: User):
    return user_controller.create(user)
    
# @user_router.post('/user')
# def post_user(user: User):
#     with Session() as session:
#         try:
#             session.add(user)
#             session.commit()
#             session.refresh(user)
#             return user
#         except Exception as e:
#             print(e)
#             return {"message": e, "status": 404}

# @user_router.delete('/user/{id}')
# def delete_user(id: int):
#     with Session() as session:
#         try:    
#             session.exec(delete(User).where(col(User.id) == id))
#             session.commit()
#             session.refresh()
#             return {"message": 203}
#         except Exception as e:
#             return {"message": e, "status": 404}

# @user_router.patch('/user/{id}')
# def patch_user(id: int, user: User):
#     with Session() as session:
#         try:
#             session\
#                 .exec(update(User)\
#                     .where(col(User.id) == id)\
#                     .values(user))
#             session.commit()
#             session.refresh(user)
#             return user
#         except Exception as e:
#             return {"message": e, "status": 404}
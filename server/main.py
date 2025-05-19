from fastapi import FastAPI
from routes import user_router, quiz_router, question_router
from prisma import Prisma
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True
)
app.include_router(user_router.router)
app.include_router(quiz_router.router)
app.include_router(question_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

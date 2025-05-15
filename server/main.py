from fastapi import FastAPI
from routes import user_router
from prisma import Prisma

app = FastAPI()
app.include_router(user_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

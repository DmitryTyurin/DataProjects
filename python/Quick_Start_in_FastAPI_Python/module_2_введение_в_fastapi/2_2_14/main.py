# Ваша задача состоит в том, чтобы расширить существующее приложение FastAPI,
# добавив новую конечную точку POST, которая принимает данные JSON, представляющие пользователя, и
# возвращает те же данные с дополнительным полем, указывающим, является ли пользователь взрослым или нет.

from fastapi import FastAPI
import uvicorn
from models import User

app = FastAPI()


@app.post("/user")
async def create_user(user: User):

    return {"name": user.name, "age": user.age, "is_adult": user.age >= 18}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

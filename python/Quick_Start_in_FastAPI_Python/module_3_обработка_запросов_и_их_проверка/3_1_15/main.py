# Ваша задача - создать конечную точку FastAPI, которая принимает POST-запрос с данными о пользователе/юзере в теле запроса. Пользовательские данные должны включать следующие поля:
#
# - `name` (str): Имя пользователя (обязательно).
# - `email` (str): адрес электронной почты пользователя (обязателен и должен иметь допустимый формат электронной почты).
# - `age` (int): возраст пользователя (необязательно, но должно быть положительным целым числом, если указано).
# - `is_subscribed` (bool): Флажок, указывающий, подписан ли пользователь на новостную рассылку (необязательно).


from fastapi import FastAPI
import uvicorn
from models import UserCreate

app = FastAPI()


@app.post("/create_user")
async def create_user(user: UserCreate):
    return user


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

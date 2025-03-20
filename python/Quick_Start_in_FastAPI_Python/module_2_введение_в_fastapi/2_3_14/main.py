# Расширьте существующее приложение FastAPI, создав конечную точку POST, которая позволяет пользователям отправлять отзывы.
# Конечная точка должна принимать данные JSON, содержащие имя пользователя и сообщение обратной связи.

from fastapi import FastAPI
import uvicorn
from models import User, Feedback

app = FastAPI()


@app.post("/user")
async def create_user(user: User):

    return {"name": user.name, "age": user.age, "is_adult": user.age >= 18}


@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    return {"message": f"Feedback received. Thank you, {feedback.name}!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

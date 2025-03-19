from fastapi import FastAPI
from models import User
import uvicorn

app = FastAPI()


user = User(name="John Doe", id=1)


@app.get("/users")
def get_user():
    return user


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

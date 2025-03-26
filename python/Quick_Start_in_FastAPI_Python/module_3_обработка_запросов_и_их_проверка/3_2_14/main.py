# Ваша задача - создать приложение FastAPI, которое реализует аутентификацию на основе файлов cookie. Выполните следующие действия:
# 1. Создайте простой маршрут входа в систему по адресу "/login", который принимает имя пользователя и пароль в качестве данных формы/JSON. Если учетные данные действительны, установите безопасный файл cookie только для HTTP с именем "session_token" с уникальным значением.
# 2. Реализуйте защищенный маршрут в "/user", который требует аутентификации с использованием файла cookie "session_token". Если файл cookie действителен и содержит правильные данные аутентификации, верните ответ в формате JSON с информацией профиля пользователя.
# 3. Если файл cookie "session_token" отсутствует или недействителен, маршрут "/user" должен возвращать ответ об ошибке с кодом состояния 401 (неавторизован) или сообщение {"message": "Unauthorized"}.

from fastapi import FastAPI, Request, Response, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import secrets
import uvicorn

app = FastAPI()


# Модель для входа
class LoginRequest(BaseModel):
    username: str
    password: str


# Модель пользователя
class UserProfile(BaseModel):
    username: str
    email: str = "user@example.com"
    full_name: str = "John Doe"


# Хранилище сессий (в реальном приложении используйте базу данных)
sessions = {}


# Проверка учетных данных (упрощенная)
def authenticate_user(username: str, password: str):
    # В реальном приложении проверяйте хэши паролей из БД
    return username == "user123" and password == "password123"


# Генератор токенов
def generate_session_token():
    return secrets.token_urlsafe(32)


# Зависимость для проверки аутентификации
def get_current_user(session_token: str = Depends(HTTPBearer(auto_error=False))):
    if not session_token:
        raise HTTPException(status_code=401, detail="Unauthorized")

    token = session_token.credentials if isinstance(session_token, HTTPAuthorizationCredentials) else session_token

    if token not in sessions:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return sessions[token]


# Маршрут для входа
@app.post("/login")
async def login(response: Response, credentials: LoginRequest):
    if not authenticate_user(credentials.username, credentials.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    # Генерируем токен сессии
    session_token = generate_session_token()
    sessions[session_token] = credentials.username

    # Устанавливаем cookie
    response.set_cookie(
        key="session_token",
        value=session_token,
        httponly=True,
        secure=True,
        max_age=3600,  # 1 час
        samesite="lax"
    )

    return {"message": "Login successful"}


# Защищенный маршрут
@app.get("/user")
async def get_user_profile(user: str = Depends(get_current_user)):
    return UserProfile(username=user)


# Маршрут для выхода
@app.post("/logout")
async def logout(response: Response, user: str = Depends(get_current_user)):
    # Удаляем сессию
    for token, username in list(sessions.items()):
        if username == user:
            del sessions[token]

    # Удаляем cookie
    response.delete_cookie("session_token")
    return {"message": "Logout successful"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
# Для этой задачи программирования вам необходимо реализовать аутентификацию на основе JWT в приложении FastAPI. Используйте библиотеку `PyJWT` для генерации и проверки токенов.
# Требования:
# 1. Создайте конечную точку FastAPI `/login`, которая принимает запросы POST с полезной нагрузкой JSON, содержащей поля "имя пользователя" (user_name) и "пароль" (password). Конечная точка должна аутентифицировать пользователя на основе предоставленных учетных данных.
# 2. Если учетные данные действительны, сгенерируйте токен JWT с соответствующим сроком действия и верните его в ответе.
# 3. Если учетные данные неверны, верните соответствующий ответ об ошибке.
# 4. Создайте защищенную конечную точку FastAPI `/protected_resource`, для которой требуется аутентификация с использованием JWT. Пользователи должны включать сгенерированный токен в заголовок `Authorization` своих запросов для доступа к этой конечной точке.
# 5. Проверьте токен JWT в заголовке `Authorization` для каждого запроса к `/protected_resource`. Если токен действителен, разрешите доступ к конечной точке и верните ответ, указывающий на успешный доступ.
# 6. Если токен недействителен, срок действия истек или отсутствует, верните соответствующий ответ об ошибке.
# Примечание: Вы можете предположить существование гипотетической функции `authenticate_user(username: str, password: str) -> bool`, которая проверяет предоставленные "имя пользователя" и "пароль" по базе данных пользователя и возвращает `True`, если учетные данные действительны, и `False` в противном случае (или создать заглушку такой функции, которая при помощи модуля random.choice возвращает True или False).*
# Пример запроса:
#
# POST /login
# Content-Type: application/json
#
# {
#   "username": "john_doe",
#   "password": "securepassword123"
# }
# Пример ответа (200 OK):
#
# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
# }
# Пример ответа (401 Unauthorized):
#
# {
#   "detail": "Invalid credentials"
# }
# !!!!Примечание: Поскольку это упрощенная задача программирования, крайне важно принять дополнительные меры безопасности и следовать рекомендациям для реальных приложений. Кроме того, обработка токенов, механизмы обновления и отзыв токенов являются важными аспектами, которые необходимо учитывать при создании готовой к работе системы аутентификации!!!!


from datetime import datetime, timedelta
from typing import Optional
import random

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import jwt
from jwt.exceptions import InvalidTokenError

app = FastAPI()
security = HTTPBearer()

# Конфигурация JWT
SECRET_KEY = (
    "your-secret-key-please-change-it"  # В продакшене используйте надежный секрет
)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Модель для входа
class LoginRequest(BaseModel):
    username: str
    password: str


# Заглушка функции аутентификации
def authenticate_user(username: str, password: str) -> bool:
    # В реальном приложении здесь должна быть проверка в БД
    # Для примера используем случайный выбор или фиксированные значения
    return random.choice([True, False])  # Для тестирования
    # Или фиксированные значения:
    # return username == "admin" and password == "secret"


# Функция создания JWT токена
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Зависимость для проверки JWT токена
async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception

    return username


# Конечная точка для входа
@app.post("/login")
async def login(login_data: LoginRequest):
    if not authenticate_user(login_data.username, login_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": login_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# Защищенная конечная точка
@app.get("/protected_resource")
async def protected_resource(current_user: str = Depends(get_current_user)):
    return {
        "message": f"Hello, {current_user}! You've accessed the protected resource.",
        "status": "success",
    }


# Обработчик ошибок для JWT
@app.exception_handler(InvalidTokenError)
async def invalid_token_exception_handler(request, exc):
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token",
        headers={"WWW-Authenticate": "Bearer"},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

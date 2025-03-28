# Реализуйте защищенную базовой аутентификацией конечную точку FastAPI `/login`, которая принимает запросы GET.
# 1. Конечная точка должна аутентифицировать пользователя на основе предоставленных учетных данных.
# 2. Используйте зависимость, чтобы проверить правильность имени пользователя и пароля.
# 3. Если учетные данные неверны, верните сообщение HTTPExceptionс кодом состояния 401 (то же самое возвращается, если учетные данные не предоставлены).
# 4. Если данные верны, верните секретное сообщение "You got my secret, welcome"
# 5. Попробуйте сначала авторизоваться с неправильными данными, а потом введите корректные данные. Для получения такой возможности (повторно авторизоваться) изучите информацию про необходимость добавления заголовка WWW-Authenticateчтобы браузер снова отображал приглашение для входа в систему.

from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import PlainTextResponse
import base64

app = FastAPI()

security = HTTPBasic()

# Храним правильные учетные данные (в реальном приложении используйте хеширование!)
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "secret"


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    # Проверяем учетные данные
    if credentials.username != CORRECT_USERNAME or credentials.password != CORRECT_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/login")
async def login(username: str = Depends(get_current_username)):
    return PlainTextResponse("You got my secret, welcome")


# Альтернативная версия без использования HTTPBasic (ручная обработка)
@app.get("/login-auth")
async def login_auth(request: Request):
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Basic "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization required",
            headers={"WWW-Authenticate": "Basic"},
        )

    try:
        # Декодируем base64
        encoded_credentials = auth_header.split(" ")[1]
        decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8")
        username, password = decoded_credentials.split(":", 1)

        if username != CORRECT_USERNAME or password != CORRECT_PASSWORD:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )

        return PlainTextResponse("You got my secret, welcome")

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
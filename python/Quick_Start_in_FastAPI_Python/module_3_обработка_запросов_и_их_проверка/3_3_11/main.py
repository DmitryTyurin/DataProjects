from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import re

app = FastAPI()

def validate_accept_language(accept_language: str) -> bool:
    """Проверяет, соответствует ли заголовок Accept-Language ожидаемому формату"""
    pattern = r'^[a-zA-Z-]+(,\s*[a-zA-Z-]+(;\s*q=[0-9.]+)?)*$'
    return bool(re.fullmatch(pattern, accept_language))

@app.get("/headers")
async def get_headers(request: Request):
    try:
        # Извлекаем необходимые заголовки
        user_agent = request.headers.get("User-Agent")
        accept_language = request.headers.get("Accept-Language")

        # Проверяем наличие обязательных заголовков
        if not user_agent:
            raise HTTPException(status_code=400, detail="User-Agent header is required")
        if not accept_language:
            raise HTTPException(status_code=400, detail="Accept-Language header is required")

        # Дополнительная проверка формата Accept-Language (необязательная часть)
        if not validate_accept_language(accept_language):
            raise HTTPException(
                status_code=400,
                detail="Accept-Language header has invalid format"
            )

        # Возвращаем ответ в формате JSON
        return JSONResponse({
            "User-Agent": user_agent,
            "Accept-Language": accept_language
        })

    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
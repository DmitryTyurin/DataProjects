from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Загружаем содержимое HTML-файла
with open("index.html", "r", encoding="utf-8") as file:
    html_content = file.read()


# Возвращаем HTML-страницу при GET-запросе к корневому маршруту
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return html_content

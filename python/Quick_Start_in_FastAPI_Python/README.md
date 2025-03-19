# Рекомендуемая структура проекта FastAPI

Рекомендуемая структура проекта FastAPI зависит от сложности вашего приложения. Для небольших проектов подойдет простая структура, а для более сложных — модульная, которая позволяет лучше организовать код и упростить его поддержку. Вот пример рекомендуемой структуры для среднего и крупного проекта:

---

## Структура проекта

```plaintext
my_fastapi_project/
├── app/                          # Основная папка приложения
│   ├── __init__.py               # Инициализация приложения
│   ├── main.py                   # Точка входа (создание экземпляра FastAPI)
│   ├── api/                      # Папка для API-роутов
│   │   ├── __init__.py
│   │   ├── v1/                   # Версия API (например, v1)
│   │   │   ├── __init__.py
│   │   │   ├── routers/          # Папка для роутеров
│   │   │   │   ├── __init__.py
│   │   │   │   ├── items.py      # Роутер для работы с элементами
│   │   │   │   └── users.py      # Роутер для работы с пользователями
│   │   │   └── models/           # Папка для моделей данных
│   │   │       ├── __init__.py
│   │   │       ├── item.py       # Модель для элементов
│   │   │       └── user.py       # Модель для пользователей
│   ├── core/                     # Папка для основной логики
│   │   ├── __init__.py
│   │   ├── config.py             # Конфигурация приложения
│   │   └── security.py           # Логика для аутентификации и авторизации
│   ├── db/                       # Папка для работы с базой данных
│   │   ├── __init__.py
│   │   ├── base.py               # Базовый класс для работы с БД
│   │   ├── session.py            # Управление сессиями БД
│   │   └── models.py             # SQLAlchemy модели (если используются)
│   ├── schemas/                  # Папка для Pydantic-схем
│   │   ├── __init__.py
│   │   ├── item.py               # Схемы для элементов
│   │   └── user.py               # Схемы для пользователей
│   └── services/                 # Папка для бизнес-логики
│       ├── __init__.py
│       ├── item_service.py       # Логика для работы с элементами
│       └── user_service.py       # Логика для работы с пользователями
├── tests/                        # Папка для тестов
│   ├── __init__.py
│   ├── test_items.py             # Тесты для работы с элементами
│   └── test_users.py             # Тесты для работы с пользователями
├── requirements.txt              # Зависимости проекта
├── .env                          # Файл для переменных окружения
└── README.md                     # Описание проекта
```

---

## Описание структуры

1. **`app/`**:
   - Основная папка приложения. 
   - Включает в себя все компоненты приложения: роутеры, модели, схемы, сервисы и т.д.


2. **`app/main.py`**:
   - Точка входа приложения. Здесь создается экземпляр FastAPI и подключаются роутеры.


3. **`app/api/`**:
   - Папка для API-роутов. Роутеры организованы по версиям (например, v1). 
   - Каждая конечная точка (endpoint) выносится в отдельный файл (например, items.py, users.py).


4. **`app/api/v1/routers/`**
   - Папка для роутеров. Здесь хранятся файлы с роутерами для API.
   - Примеры:
     - items.py — роутер для работы с элементами.
     - users.py — роутер для работы с пользователями.


5. **`app/api/v1/models/`**
   - Папка для моделей данных. Здесь хранятся файлы с моделями данных.
   - Примеры:
     - item.py — модель для элементов.
     - user.py — модель для пользователей.

6. **`app/core/`**
   - Папка для основной логики приложения: конфигурация, безопасность, утилиты.


7. **`app/db/`**
   - Папка для работы с базой данных. Включает модели, сессии и базовый класс для работы с БД.


8. **`app/schemas/`**
   - Папка для Pydantic-схем, которые используются для валидации входных и выходных данных.


9. **`app/services/`**
   - Папка для бизнес-логики. Здесь находятся сервисы, которые обрабатывают запросы и взаимодействуют с базой данных.


10. **`tests/`**
    - Папка для тестов. Тесты организованы по модулям (например, `test_items.py`, `test_users.py`).


11. **`requirements.txt`**
    - Файл с зависимостями проекта.


12. **`.env`**
    - Файл для хранения переменных окружения (например, секретные ключи, настройки БД).


13. **`README.md`**
    - Описание проекта, инструкции по установке и запуску.

---

### Примеры кода
### Пример `app/main.py`
```python
from fastapi import FastAPI
from app.api.v1.routers import items, users

app = FastAPI()
app.include_router(items.router, prefix="/api/v1/items", tags=["items"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
```

### Пример `app/api/v1/routers/items.py`
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.v1.models.item import Item
from app.schemas.item import ItemCreate, ItemResponse

router = APIRouter()

@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
```

### Пример `app/api/v1/models/item.py`
```python
from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
```    

### Пример `app/db/base.py`
```python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
```

### Пример `app/db/session.py`
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"  # для SQLite

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### Пример `app/schemas/item.py`
```python
from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str
```

### Пример `app/services/item_service.py`
```python
from sqlalchemy.orm import Session
from app.api.v1.models.item import Item
from app.schemas.item import ItemCreate, ItemResponse

class ItemService:
    @staticmethod
    def create_item(db: Session, item: ItemCreate) -> ItemResponse:
        db_item = Item(name=item.name, description=item.description)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return ItemResponse(id=db_item.id, name=db_item.name, description=db_item.description)
```

---

1. **`Модульность:`** 
   - Код разделен на логические модули, что упрощает поддержку и расширение.
2. **`Масштабируемость:`** 
   - Легко добавлять новые функции и версии API.
3. **`Тестируемость:`** 
   - Тесты изолированы и легко запускаются.
4. **`Чистота кода:`** 
   - Логика разделена на слои (роутеры, модели, схемы, сервисы).
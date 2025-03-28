# Для этой задачи программирования вам необходимо реализовать управление доступом на основе ролей в приложении FastAPI. Предположим, что аутентификация на основе JWT уже реализована, и пользователям назначаются роли в процессе регистрации.
# Требования:
# 1. Создайте как минимум три роли: "администратор", "пользователь" и "гость" (admin, user, guest). Определите соответствующие разрешения для каждой роли. Например, "администратор" может иметь полные разрешения CRUD, в то время как "пользователь" может читать и обновлять ресурсы, а "гость" имеет ограниченный доступ только для чтения.
# 2. Реализуйте авторизацию на основе ролей для ваших конечных точек FastAPI. Используйте внедрение зависимостей или авторизацию на основе декоратора, чтобы проверить роль пользователя, прежде чем разрешить доступ к определенным конечным точкам.
# 3. Создайте конечную точку FastAPI `/protected_resource`, для которой требуется аутентификация. Убедитесь, что только пользователи с соответствующей ролью (например, "администратор" или "пользователь") могут получить доступ к этой конечной точке.
# 4. Для каждой роли создайте определенные конечные точки API, которые демонстрируют разрешения этой роли. Например, роль "администратор" может иметь конечную точку для создания ресурса, в то время как роль "пользователь" может только читать и обновлять существующие ресурсы.
# 5. Протестируйте свою реализацию RBAC, отправляя запросы к различным конечным точкам с разными ролями пользователей. Убедитесь, что доступ надлежащим образом ограничен в зависимости от роли пользователя.
# Примечание: Для этой задачи вы можете использовать словари Python или простое хранилище данных в памяти для хранения ролей и связанных с ними разрешений. В реальном сценарии вы обычно интегрируете RBAC с базой данных вашего приложения.

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

app = FastAPI()
security = HTTPBearer()


# Определение ролей
class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


# Модель пользователя
class User(BaseModel):
    username: str
    password: str  # В реальном приложении храните только хеш
    roles: List[Role]


# Хранилище пользователей (в памяти)
users_db = {
    "admin": User(
        username="admin",
        password="adminpass",  # В реальном приложении никогда не храните пароли в открытом виде
        roles=[Role.ADMIN]
    ),
    "user1": User(
        username="user1",
        password="userpass",
        roles=[Role.USER]
    ),
    "guest1": User(
        username="guest1",
        password="guestpass",
        roles=[Role.GUEST]
    ),
}


# Модель для ресурсов
class Resource(BaseModel):
    id: int
    name: str
    content: str


# Хранилище ресурсов (в памяти)
resources_db = [
    Resource(id=1, name="Resource 1", content="Sensitive data 1"),
    Resource(id=2, name="Resource 2", content="Sensitive data 2"),
]


# Зависимость для проверки ролей
def has_required_roles(required_roles: List[Role]):
    async def role_checker(credentials: HTTPAuthorizationCredentials = Depends(security)):
        # В реальном приложении здесь должна быть проверка JWT токена
        # и извлечение информации о пользователе
        username = credentials.credentials  # Вместо токена используем username для упрощения

        if username not in users_db:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        user = users_db[username]
        user_roles = user.roles

        # Проверяем, есть ли у пользователя хотя бы одна из требуемых ролей
        if not any(role in required_roles for role in user_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have permission to access this resource",
            )

        return user

    return role_checker


# Конечные точки API

# Общий защищенный ресурс - доступен всем аутентифицированным пользователям
@app.get("/protected_resource")
async def get_protected_resource(user: User = Depends(has_required_roles([Role.ADMIN, Role.USER, Role.GUEST]))):
    return {"message": "This is a protected resource", "user": user.username}


# Только для администраторов
@app.post("/resources", status_code=status.HTTP_201_CREATED)
async def create_resource(resource: Resource, user: User = Depends(has_required_roles([Role.ADMIN]))):
    resources_db.append(resource)
    return {"message": "Resource created successfully", "resource": resource}


# Для администраторов и пользователей
@app.put("/resources/{resource_id}")
async def update_resource(
        resource_id: int,
        updated_resource: Resource,
        user: User = Depends(has_required_roles([Role.ADMIN, Role.USER]))
):
    for idx, res in enumerate(resources_db):
        if res.id == resource_id:
            resources_db[idx] = updated_resource
            return {"message": "Resource updated successfully", "resource": updated_resource}

    raise HTTPException(status_code=404, detail="Resource not found")


# Для всех ролей (но только чтение)
@app.get("/resources")
async def get_all_resources(user: User = Depends(has_required_roles([Role.ADMIN, Role.USER, Role.GUEST]))):
    return {"resources": resources_db}


# Только для гостей (пример специфичной функциональности)
@app.get("/public_info")
async def get_public_info(user: User = Depends(has_required_roles([Role.GUEST]))):
    return {"message": "This is public information available to guests"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
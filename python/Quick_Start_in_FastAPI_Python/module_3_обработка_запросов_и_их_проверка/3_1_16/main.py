# Ваша задача - создать приложение FastAPI, которое обрабатывает запросы, связанные с продуктами (товарами).
# Приложение должно иметь две конечные точки:

from fastapi import FastAPI, HTTPException
from typing import List, Optional
import uvicorn

app = FastAPI()

sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99,
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99,
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99,
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99,
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99,
}

sample_products = [
    sample_product_1,
    sample_product_2,
    sample_product_3,
    sample_product_4,
    sample_product_5,
]


@app.get("/product/{product_id}")
async def get_product(product_id: int):
    """Получить информацию о продукте по его ID"""
    for product in sample_products:
        if product["product_id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.get("/products/search")
async def search_products(
    keyword: str, category: Optional[str] = None, limit: int = 10
) -> List[dict]:
    results = []

    # Приводим ключевое слово к нижнему регистру для регистронезависимого поиска
    keyword_lower = keyword.lower()

    for product in sample_products:
        # Проверяем, содержит ли название продукта ключевое слово
        if keyword_lower in product["name"].lower():
            # Если указана категория, проверяем совпадение
            if category is None or product["category"].lower() == category.lower():
                results.append(product)
                # Прерываем, если достигнут лимит
                if len(results) >= limit:
                    break

    return results


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

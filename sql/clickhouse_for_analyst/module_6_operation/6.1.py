# В данном уроке вам предстоит загрузить в Clickhouse CSV файл с помощью Python или же командной строки!
# У вас есть право выбора что лучше использовать. Однако записать файл можно только через HTTP протокол.

import requests

USER = ""
PASSWORD = ""
URL = "http://158.160.116.58:8123"
TABLE = "sandbox.user_active_http_2"

FILE_PATH = "csvjson.csv"


def create_table(user: str, password: str | int, url: str, table: str) -> None:
    query = f"""
        create table if not exists {table} 
        (
            id                  UInt32                  comment 'id пользователя',
            name                String                  comment 'имя пользователя',
            value               Float64                 comment 'значение',
            is_active           Bool                    comment 'активный пользователь',
            key                 String                  comment 'ключ',
            list                Array(Int64)            comment 'список'
        )
        engine = MergeTree()
        order by (tuple())
        """

    response = requests.post(
        url, params={"query": query, "user": user, "password": password}
    )

    if response.status_code == 200:
        print(f"Таблица {table} успешно создана")
    else:
        print(f"Ошибка при создании таблицы: {response.text}")


def insert_data(
    user: str, password: str | int, url: str, table: str, file_path: str
) -> None:
    with open(file_path, "rb") as file:
        data = file.read().decode("utf-8")

    query = f"""
        insert into {table} format CSVWithNames
            """
    headers = {"X-ClickHouse-User": user, "X-ClickHouse-Key": password}

    response = requests.post(url, data=data, headers=headers, params={"query": query})

    if response.status_code == 200:
        print(f"Таблица {table} заполнена")
    else:
        print(f"Ошибка при заполнении таблицы: {response.text}")


def select_data(user: str, password: str | int, url: str, table: str) -> None:

    query = f"""
        select round(sum(value)) as sum_value
        from {table}
        """

    response = requests.post(
        url, params={"query": query, "user": user, "password": password}
    )

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Ошибка вставки: {response.text}")


def main():
    create_table(USER, PASSWORD, URL, TABLE)
    insert_data(USER, PASSWORD, URL, TABLE, FILE_PATH)
    select_data(USER, PASSWORD, URL, TABLE)


if __name__ == "__main__":
    main()

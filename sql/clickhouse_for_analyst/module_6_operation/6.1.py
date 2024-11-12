# В данном уроке вам предстоит загрузить в Clickhouse CSV файл с помощью Python или же командной строки!
# У вас есть право выбора что лучше использовать. Однако записать файл можно только через HTTP протокол.

import requests

USER = ""
PASSWORD = ""
URL = ""
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


# В данном уроке вам предстоит загрузить в Clickhouse CSV файл с помощью clickhouse-driver!
# При решении вы столкнетесь с проблемой конвертации типов данных. Это можно обойти использовав такой подход
# select * from url( ... )
# Тем не менее есть вариант решения задачи только через Python код. Будет принято любое решение.
# Формат ответа:
# В качестве ответа прислать sum(value) округлить до целых в любую сторону

from clickhouse_driver import Client

USER = ""
PASSWORD = ""
HOST = ""
PORT = ""
DATABASE = "sandbox"
TABLE = "sandbox.user_active_url_1"

FILE_PATH = "csvjson.csv"

client = Client(
    host=HOST,
    port=PORT,
    user=USER,
    password=PASSWORD,
    database=DATABASE,
    settings={"use_numpy": True},
)


def create_table(client: Client, table: str) -> None:
    query = f"""
        create table if not exists {table}
        (
            id                  UInt32                  comment 'id пользователя',
            name                String                  comment 'имя пользователя',
            value               Float64                 comment 'значение',
            is_active           Bool                    comment 'активный пользователь',
            key                 UInt32                  comment 'ключ',
            list                Array(Int32)            comment 'список'
        )
        engine = MergeTree()
        order by (tuple())
        
        """
    client.execute(query)
    print(f"Таблица {table} успешно создана")


def insert_data(client: Client, table: str, file_path: str) -> None:
    import clickhouse_driver
    import pandas as pd

    data = pd.read_csv(file_path)

    for column in data.columns:
        print(f"Тип столбца {column}: {data[column].dtype}")

    query = f"""
        insert into {table} 
        values 
        """
    try:
        client.insert_dataframe(query, data)
    except clickhouse_driver.errors.TypeMismatchError as e:
        print(e)


def select_data(client: Client, table: str) -> None:
    query = f"""
        select round(sum(value)) as sum_value
        from {table}
        """
    result = client.execute(query)
    print(result)


def main():
    with client:
        create_table(client, TABLE)
        insert_data(client, TABLE, FILE_PATH)
        select_data(client, TABLE)


if __name__ == "__main__":
    main()

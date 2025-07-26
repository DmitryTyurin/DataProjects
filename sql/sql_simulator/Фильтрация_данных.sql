-- Напишите SQL-запрос к таблице products и выведите всю информацию о товарах, цена которых не превышает 100 рублей. Результат отсортируйте по возрастанию id товара.
-- Поля в результирующей таблице: product_id, name, price

select
    product_id,
    name,
    price
from products
where price <= 100
order by
    product_id asc


-- Отберите пользователей женского пола из таблицы users. Выведите только id этих пользователей. Результат отсортируйте по возрастанию id.
-- Добавьте в запрос оператор LIMIT и выведите только 1000 первых id из отсортированного списка.
-- Поле в результирующей таблице: user_id

select user_id
from users
where sex = 'female'
order by user_id asc
limit 1000


-- Отберите из таблицы user_actions все действия пользователей по созданию заказов, которые были совершены ими после полуночи 6 сентября 2022 года.
-- Выведите колонки с id пользователей, id созданных заказов и временем их создания.
-- Результат должен быть отсортирован по возрастанию id заказа.
-- Поля в результирующей таблице: user_id, order_id, time

select
    user_id,
    order_id,
    time
from user_actions
where
    cast(time as date) > '2022-09-05'
    and action = 'create_order'
order by order_id asc



--Выведите все записи из таблицы products.
--Поля в результирующей таблице: product_id, name, price


SELECT product_id,
       name,
       price
FROM   products


--Выведите все записи из таблицы products, отсортировав их по наименованиям товаров в алфавитном порядке, т.е. по возрастанию. Для сортировки используйте оператор ORDER BY.
--Поля в результирующей таблице: product_id, name, price

SELECT product_id,
       name,
       price
FROM   products
ORDER BY name asc


--Отсортируйте таблицу courier_actions сначала по колонке courier_id по возрастанию id курьера, потом по колонке action (снова по возрастанию), а затем по колонке time, но уже по убыванию — от самого последнего действия к самому первому. Не забудьте включить в результат колонку order_id.
--Добавьте в запрос оператор LIMIT и выведите только первые 1000 строк результирующей таблицы.
--Поля в результирующей таблице: courier_id, order_id, action, time

SELECT courier_id,
       order_id,
       action,
       time
FROM   courier_actions
ORDER BY courier_id asc, action asc, time desc limit 1000 ;


--Используя операторы SELECT, FROM, ORDER BY и LIMIT, определите 5 самых дорогих товаров в таблице products, которые доставляет наш сервис. Выведите их наименования и цену.
--Поля в результирующей таблице: name, price

SELECT name,
       price
FROM   products
ORDER BY price desc limit 5


--Как в прошлом задании определите 5 самых дорогих товаров в таблице products. Но теперь колонки name и price переименуйте соответственно в product_name и product_price.
--Поля в результирующей таблице: product_name, product_price

SELECT name as product_name,
       price as product_price
FROM   products
ORDER BY price desc limit 5


--Используя операторы SELECT, FROM, ORDER BY и LIMIT, а также функцию LENGTH, определите товар с самым длинным названием в таблице products. Выведите его наименование, длину наименования в символах, а также цену этого товара. Колонку с длиной наименования в символах назовите name_length.
--Поля в результирующей таблице: name, name_length, price

SELECT name,
       length(name) as name_length,
       price
FROM   products
ORDER BY name_length desc limit 1


--Примените последовательно функции UPPER и SPLIT_PART к колонке name и преобразуйте наименования товаров в таблице products так, чтобы от названий осталось только первое слово, записанное в верхнем регистре. Колонку с новым названием, состоящим из первого слова, назовите first_word.
--В результат включите исходные наименования товаров, новые наименования из первого слова, а также цену товаров. Результат отсортируйте по возрастанию исходного наименования товара в колонке name.
--Поля в результирующей таблице: name, first_word, price

SELECT name,
       split_part(upper(name), ' ', 1) as first_word,
       price
FROM   products
ORDER BY name asc


--Измените тип колонки price из таблицы products на VARCHAR. Выведите колонки с наименованием товаров, ценой в исходном формате и ценой в формате VARCHAR. Новую колонку с ценой в новом формате назовите price_char.
--Результат отсортируйте по возрастанию исходного наименования товара в колонке name. Количество выводимых записей не ограничивайте.
--Поле в результирующей таблице: name, price, price_char

SELECT name,
       price,
       cast(price as varchar) as price_char
FROM   products
ORDER BY name asc


--Для первых 200 записей из таблицы orders выведите информацию в следующем виде (обратите внимание на пробелы):
--Заказ № [id заказа] создан [дата]
--Полученную колонку назовите order_info.

SELECT concat('Заказ № ', order_id, ' создан ', creation_time::date) as order_info
FROM   orders limit 200



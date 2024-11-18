--Напишите запрос для получения общего количество заказов  по каждому клиенту.
--В результате должна получиться таблица с customer_id и столбцом количества заказов у этого id (давайте назовем его total_orders)

select customer_id, count(order_id) as total_orders
from orders
group by customer_id;


--Напишите запрос для получения общего количество заказов  по каждому продукту.
--В результате должна получиться таблица с product_id и столбцом количества заказов у этого id (давайте тоже назовем его  total_orders).

select product_id, count(order_id) as total_orders
from orders
group by product_id;


--Найти товары, которые были заказаны более 5 раз. Вывести id и количество.

select product_id, count(order_id) as total_orders
from orders
group by product_id
having count(order_id) > 5;
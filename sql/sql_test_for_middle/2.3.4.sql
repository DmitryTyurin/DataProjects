--Команда по развитию клиентов хочет понять, какие клиенты оформили три и более заказов. Это поможет запустить специальную программу лояльности для активных клиентов.
--Нужно посчитать количество заказов на каждого клиента и вывести только тех, у кого заказов три и более.

with
join_data as
(
    select c.customer_id, c.customer_name, o.order_id
    from customers c
    left join orders o using(customer_id)
)
select
    customer_name,
    count(order_id) as order_count
from join_data
group by customer_name
having order_count >= 3
;

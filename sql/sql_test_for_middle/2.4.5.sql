--Найти всех клиентов, которые сделали заказ в день акции — 1 мая 2025 года (это и считается участием в акции).
--Далее проверить: кто из этих клиентов совершил ещё один заказ с 2 по 15 мая включительно.
--Нужно вернуть только первую дату такого повторного заказа.

with
action_data as
(
    select distinct
        client_id,
        order_date
    from orders
    where order_date = '2025-05-01'
),
return_orders as
(
    select
        o.client_id,
        c.name,
        c.segment,
        min(o.order_date) as return_date
        from orders o
        left join clients c using (client_id)
        where o.order_date between '2025-05-02' and '2025-05-15'
            and o.client_id in (select client_id from action_data)
        group by
            o.client_id,
            c.name,
            c.segment

)
select *
from return_orders
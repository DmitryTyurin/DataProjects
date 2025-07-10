--В e-commerce компании аналитики хотят понять, какие клиенты возвращались с повторным заказом в течение 7 дней после предыдущего.
--Это поможет выделить вовлечённых пользователей и спрогнозировать повторные покупки.


with
lead_data as
(
    select
        order_id,
        client_id,
        order_date,
        lead(order_date) over (partition by client_id order by order_date) as next_order
    from orders
)
select
    client_id,
    order_date,
    next_order
from lead_data
where datediff(next_order, order_date) <= 7
order by client_id
;
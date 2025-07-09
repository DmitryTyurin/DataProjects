--Бизнес-аналитикам важно понять, когда клиент впервые совершал покупку. Это поможет в моделировании жизненного цикла клиента и планировании маркетинговых акций.
--Найдите ID клиента, дату и сумму первого заказа для каждого клиента.

with
rank_data as
(
    select
        customer_id,
        order_date,
        total_amount,
        row_number() over(partition by customer_id order by order_date) as rn
    from orders
)
select
    customer_id,
    order_date,
    total_amount
from rank_data
where rn = 1
;

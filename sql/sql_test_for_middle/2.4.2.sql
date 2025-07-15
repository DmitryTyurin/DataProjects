--Бизнесу важно понимать, какие клиенты совершают повторные заказы в течение 2 дней — это может сигнализировать о срочной потребности или высокой лояльности.
--Найдите такие случаи: когда клиент оформил заказ, а предыдущий заказ был не более 2 дней назад.

with
data as
(
    select
        client_id,
        order_date,
        lag(order_date) over (partition by client_id order by order_date) as prev_date
    from orders
)
select
    client_id,
    order_date,
    prev_date,
    datediff(order_date, prev_date) as days_between
from data
where datediff(order_date, prev_date) <= 2
;
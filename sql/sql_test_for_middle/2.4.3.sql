--Аналитикам интернет-магазина нужно отслеживать динамику трат клиентов — например, смотреть, как меняется их средний чек со временем.
--Для каждого заказа рассчитайте среднее значение total_amount по текущему и двум предыдущим заказам этого же клиента. Результат округлите до целого числа.

select
    client_id,
    order_date,
    total_amount,
    round(avg(total_amount) over (partition by client_id order by order_date rows between 2 preceding and current row)) as avg_amount
from orders
;
--Напишите запрос для размещения рейтинга заказов по общей стоимости. Ответ должен содержать order_id,  order_rank

with total_sum_order_table as
    (
        select o.order_id, sum(o.quantity * price_per_unit) as total_sum_order_id
        from orders o
            left join products p using(product_id)
        group by o.order_id
     )
select order_id, RANK() OVER(PARTITION BY total_sum_order_id) as order_rank
from total_sum_order_table;
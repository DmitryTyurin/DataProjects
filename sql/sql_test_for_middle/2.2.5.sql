--Финансовый отдел хочет узнать, какая покупка была самой дорогой. Необходимо найти заказ с максимальной суммой и вывести его номер, имя клиента и сумму заказа.

with
max_data as
(
    select max(total_amount) as max_amount
    from orders
)
select
    o.order_id,
    o.customer_name,
    o.total_amount
from orders o, max_data m
where total_amount in (max_amount)
;
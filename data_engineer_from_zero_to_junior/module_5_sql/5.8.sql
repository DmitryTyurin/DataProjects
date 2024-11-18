--Напишите верный запрос чтобы найти все заказы, сделанные клиентом с именем "Алексей Алексеев".
--Результат должен содержать:
--order_id, product_name

select o.order_id, p.product_name
from orders o
    left join customers c using(customer_id)
    left join products p using(product_id)
where c.name = 'Алексей Алексеев';


--Напишите запрос, чтобы определить общую стоимость заказов для каждого клиента за весь период, отсортированную по стоимости в убывающем порядке.

with total_cost_table as
    (
        select o.customer_id, sum(p.price_per_unit * o.quantity) as total_cost
         from orders o
             left join products p on o.product_id = p.product_id
        group by o.customer_id
    )
select c.name as name, tct.total_cost as total_cost
from customers c
    left join total_cost_table tct on tct.customer_id = c.customer_id
order by total_cost desc;


--Напишите верный запрос чтобы найти товары, которые были заказаны только одним клиентом.

select p.product_name
from orders o
    left join customers c using(customer_id)
    left join products p using(product_id)
group by p.product_name
having count(distinct c.name) = 1;
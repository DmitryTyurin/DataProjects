--Напишите запрос для выбора всех заказов, где количество товаров больше среднего количества товаров всех заказов.
--В результатах должны быть order_id, customer_id, product_id и quantity.

select order_id,
    customer_id,
    product_id,
    quantity
from orders
where quantity > (select avg(quantity) from orders);


--Напишите запрос для выбора всех заказов, где товар имеет цену более 10.00.
--В результатах должны быть order_id, customer_id, product_id, quantity.

select order_id,
    customer_id,
    product_id,
    quantity
from orders
where product_id in (
	select product_id
	from products
	where price_per_unit > 10
	);


--Напишите запрос для выбора заказов, где количество товаров выше среднего количества товаров для каждого клиента.
--В результатах должны быть order_id, customer_id, product_id, quantity.

select o.order_id,
       o.customer_id,
       o.product_id,
       o.quantity
from   orders o
    join (
      select customer_id,
             avg(quantity) as avg_quantity
      from   orders
      group by customer_id
                            ) t on o.customer_id = t.customer_id
where  o.quantity > t.avg_quantity;
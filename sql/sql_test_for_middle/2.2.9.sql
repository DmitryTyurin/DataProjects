--В отделе продаж хотят увидеть список всех активных заказов, в которых фигурируют товары из категории «Электроника».


select
	o.order_id,
	p.product_name
from orders o
join products p on
        o.product_id = p.product_id
        and p.category = 'Электроника'
        and o.status = 'active'
;
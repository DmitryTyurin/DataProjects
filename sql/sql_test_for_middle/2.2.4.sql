--В системе интернет-магазина необходимо определить, какие товары из категории «Электроника» были заказаны.

select
    o.order_id,
    p.product_name
from orders o
inner join products p using (product_id)
    and p.category = 'Электроника'
;
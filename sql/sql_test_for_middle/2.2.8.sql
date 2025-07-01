--В отделе аналитики хотят проанализировать ассортимент в категории «Бытовая техника».
--Необходимо выбрать все товары из этой категории.

select
	product_name,
	category
from products
where category = 'Бытовая техника'
order by product_name
;
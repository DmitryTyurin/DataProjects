--В онлайн-магазине нужно собрать ежедневную выручку. Необходимо сгруппировать заказы по дате и рассчитать сумму всех заказов на каждую дату.

select
	order_date,
	sum(total_amount) as daily_total
from orders
group by order_date
;
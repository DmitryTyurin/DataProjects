--Руководство хочет узнать, в каких регионах общий доход от заказов превышает 2000 единиц.
--Покажите только те регионы, где сумма заказов больше 2000.

select
    region,
    sum(total_amount) as total_income
from orders
group by region
having total_income > 2000
;
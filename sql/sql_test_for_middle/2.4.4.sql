--Команда менеджеров анализирует продажи, чтобы понять, какие товары приносят больше всего выручки в каждой категории.
--Это нужно для принятия решений по закупке и рекламе.
--Найдите товары с наибольшей выручкой в каждой категории — даже если их несколько.

with
data_1 as
(
    select
        p.category,
        p.product_name,
        sum(o.quantity * o.price) as revenue,
        row_number() over(partition by category order by sum(o.quantity * o.price) desc) as rn
    from orders o
        left join products p using(product_id)
    group by p.category, p.product_name
)
select
    category,
    product_name,
    revenue
from data_1
where rn = 1
;
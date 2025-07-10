--Команда по аналитике в e-commerce-компании исследует поведение клиентов при повторных покупках.
--Их интересует, меняют ли покупатели категории товаров между заказами.
--
--Нужно найти случаи, когда клиент оформил заказ, и категория нового товара отличалась от предыдущей.

with
join_data as
(
    select
        o.customer_id,
        o.order_date,
        lag(p.category) over(partition by o.customer_id order by o.order_date) as prev_category,
        p.category  as current_category
    from orders o
    left join products p using(product_id)
)
select
    customer_id,
    order_date,
    prev_category,
    current_category
from join_data
where prev_category != current_category
;

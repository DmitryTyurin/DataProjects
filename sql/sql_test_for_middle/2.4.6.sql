--Команда категорийных менеджеров хочет найти товары, которые стоят дороже большинства товаров в своей категории.
--Для этого необходимо определить медиану цен по каждой категории и отобрать товары, которые находятся выше медианы (то есть входят в верхнюю половину по стоимости).

with
median_data as
(
    select
        category,
        product_name,
        price,
        percent_rank() over (partition by category order by price) as pr
    from products
)
select
    category,
    product_name,
    price
from median_data
where pr > 0.5

--Задание делится на 2 части, создание необходимой таблицы и генерация данных + вставка в таблицу.
--В данном задании вам нужно будет создать таблицу с движком MergeTree со следующими параметрами.
--В полученную таблицу вставьте набор сгенерированных данных, скрипт генерации можете найти по данной ссылке.
--Чтобы вставить данные используйте такой код
--Далее посчитайте сумму по полю sale_amount это и будет ответ.

-- drop table if exists sandbox.sales_dtyurin
create table if not exists sandbox.sales_dtyurin
(
    sale_date 				String			    comment 'дата продажи',
    product_id 				Int64 				comment 'идентификатор продукта',
    product_category 		String 				comment 'категория продукта',
    sale_amount 			Int64	default 0 	comment 'сумма продажи',
    sale_quantity 			Int64 				comment 'количество продаж',
    customer_id 			Int64	 			comment	'идентификатор покупателя',
    store_id				Int64 				comment 'идентификатор магазина'
)
engine = MergeTree
partition by toYYYYMM(sale_date)
order by (sale_date, product_id, customer_id)
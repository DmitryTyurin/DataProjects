--Задание делится на 2 части, создание необходимой таблицы и генерация данных + вставка в таблицу.
--В данном задании вам нужно будет создать таблицу с движком MergeTree со следующими параметрами.
--В полученную таблицу вставьте набор сгенерированных данных, скрипт генерации можете найти по данной ссылке.
--Чтобы вставить данные используйте такой код
--Далее посчитайте сумму по полю sale_amount это и будет ответ.

-- drop table if exists sandbox.sales_dtyurin
create table if not exists sandbox.sales_dtyurin
(
    sale_date 				DateTime			                    comment 'дата продажи',
    product_id 				Int64 				                    comment 'идентификатор продукта',
    product_category 		String 				                    comment 'категория продукта',
    sale_amount 			Int64	default 0 	                    comment 'сумма продажи',
    sale_quantity 			Int64 				                    comment 'количество продаж',
    customer_id 			Int64	 			                    comment	'идентификатор покупателя',
    store_id				Int64 				                    comment 'идентификатор магазина'
)
engine = MergeTree
partition by toYYYYMM(sale_date)
order by (sale_date, product_id, customer_id)


--Создайте таблицу аналогичную предыдущей с движком ReplacingMergeTree и ключём сортировки product_category
-- drop table if exists sandbox.sales_5_1_2
create table if not exists sandbox.sales_5_1_2
(
    sale_date 				DateTime			                    comment 'дата продажи',
    product_id 				Int64 				                    comment 'идентификатор продукта',
    product_category 		String 				                    comment 'категория продукта',
    sale_amount 			Int64	default 0 	                    comment 'сумма продажи',
    sale_quantity 			Int64 				                    comment 'количество продаж',
    customer_id 			Int64	 			                    comment	'идентификатор покупателя',
    store_id				Int64 				                    comment 'идентификатор магазина'
)
engine = ReplacingMergeTree
partition by toYYYYMM(sale_date)
order by (product_category)


--Создайте таблицу аналогичную предыдущей с движком AggregatingMergeTree и ключём сортировки product_category
--Укажите поля агрегации
--sale_amount как SUM
--customer_id как any

create table sandbox.sales_aggregated
(
    sale_date 				DateTime								comment 'дата продажи',
    product_id 				Int64 									comment 'идентификатор продукта',
    product_category 		String 									comment 'категория продукта',
    sale_amount 			SimpleAggregateFunction(sum, Float64) 	comment 'сумма продажи',
    sale_quantity 			Int64 									comment 'количество продаж',
    customer_id 			SimpleAggregateFunction(any, UInt32)	comment	'идентификатор покупателя',
    store_id				Int64 									comment 'идентификатор магазина'
)
engine = AggregatingMergeTree()
partition by toYYYYMM(sale_date)
order by (product_category)


--Итак, у нас есть null таблица, такие таблицы не хранят данные, но в них может смотреть MV чтобы разбирать поступающий поток событий.
--В такую таблицу льется поток json, и мы хотим повесить MV чтобы она разбирала json и вставляла его отдельно по колонкам.
--Вам необходимо написать запрос на создание такой MV.

--drop table if exists sandbox.user_active__mv;
create materialized view if not exists sandbox.user_active__mv
(
	id 				UInt32 				                            comment 'id пользователя',
	name 			String 				                            comment 'имя пользователя',
	value 			Float64 			                            comment 'значение',
	is_active 		Bool 				                            comment 'активный пользователь',
	key 			Int64 				                            comment 'ключ',
	list 			Array(Int64) 		                            comment 'список'
)
engine = MergeTree
order by (tuple())
as
select
	JSONExtractInt(json, 'id') as id,
	JSONExtractString(json, 'name') as name,
	JSONExtractFloat(json, 'value') as value,
	JSONExtractBool(json, 'is_active') as is_active,
	JSONExtractInt(json, 'key') as key,
	JSONExtractString(json, 'list') as list
from sandbox.raw200
--Это простое задание, вам дана таблица с типом Log с данными, вам необходимо создать аналогичную таблицу MergeeTree(партиции и сортировку выбрать ан свое усмотрение),
--с дополнительным полем insert_timeв котором будет лежать дата вставки в таблицу, например использую now()

--drop table if exists sandbox.log_to_insert
create table if not exists sandbox.log_to_insert
(
    event_time 		DateTime,
    user_id 		String,
    country_code	String,
    insert_time		DateTime default now()

)
engine = MergeTree
partition by toYYYYMM(event_time)
order by (user_id, event_time)

--drop table if exists sandbox.log_to_insert__mv
create materialized view if not exists sandbox.log_to_insert__mv
to sandbox.log_to_insert
(
    event_time 		DateTime,
    user_id 		String,
    country_code	String

)
as
select *
from sandbox.log


--В данном задании вам необходимо будет скачать данные из S3.
--В интернете есть доступный для вас инстанс MiniO (S3). Куда вы можете сделать запрос.

--drop table if exists sandbox.s3_currency
create table if not exists sandbox.s3_currency
(
    currency 		String,
    value 			Int64,
    date 			String
)
engine = S3('http://minio:9000/clickhouse/*',
 			'...', --логин
 			'...', --пароль
 			'CSVWithNames'
 			)


--В данном задании вам необходимо будет скачать данные из S3.
--В интернете есть доступный для вас инстанс MiniO (S3). Куда вы можете сделать запрос.

--drop table if exists sandbox.s3_currency_pq
create table if not exists sandbox.s3_currency_pq
(
    currency 		String,
    value 			Int64,
    date 			String
)
engine = S3('http://minio:9000/clickhousepq/*',
 			'...', --логин
 			'...', --пароль
 			'Parquet'
 			)


--Предлагаю в этом задании вам самостоятельно изучить движок для чтения данных по URL.
--Вам необходимо выгрузить таблицу по этому адресу https://raw.githubusercontent.com/datanlnja/clickhouse_course/main/5.2/5

--drop table if exists sandbox.s3_currency_url_2
create table if not exists sandbox.s3_currency_url_2
(
    currency 		String,
    value 			Int64,
    date 			String
)
engine = URL('https://raw.githubusercontent.com/datanlnja/clickhouse_course/main/5.2/5',
			 'CSVWithNames'
			)


--Напишите запрос которые объединит данные с помощью joinGet и выведет размер популяции для каждой строки, в качестве ответа вставьте сумму по получившемуся столбцу.

select sum(joinGet('sandbox.geo', 'population', country_code)) as population
from sandbox.log300
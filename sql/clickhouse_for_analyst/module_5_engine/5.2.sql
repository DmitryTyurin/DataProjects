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
--В данном задании вам необходимо написать запрос к системным таблицам который: выведет размеры всех таблиц в килобайтах!
--Просьба решать данное задание в этой среде! http://158.160.116.58:8123/
--Написать размер таблицы log_mt в килобайтах.

select round(sum(bytes_on_disk) / 1024) as size_in_kb
from system.parts
where table = 'log_mt'


--В данном задании вам необходимо написать запрос к системным таблицам который:
--выведет для таблицы log_mt запрос select с самым большим количеством использования памяти memory_usage за дату 2024-09-08

select memory_usage
from system.query_log
where 1
	and query_kind = 'Select'
	and has(tables, 'default.log_mt')
	and toDate(event_date) = '2024-09-08'
order by memory_usage desc
limit 1;
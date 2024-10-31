--Потренируемся в парсинге JSON Вам дана таблица с большим JSON, вам необходимо её распарсить и произвести несколько вычислений.
--Парсинг (достаньте поля JSON документа следующим образом):
--value - как Float
--is_active - как Bool
--key - как String и преобразовать в Int64
--list - как Array

--Дополнительные вычисления (проведите небольшие вычисления для получения ответа):
--По value посчитать сумму
--По listсначала просуммировать по каждому массиву,
--Нужно будет поменять тип лежащих данных на Int64 (вам может помочь arrayMap)
--Возьмите среднее avg по получившейся колонке
--По key преобразовать в Int64 затем взять среднее avg

with
$$
Tuple(
id				Int64,
name			String,
value			Float64,
is_active		Bool,
key				String,
list			Array(Int64)
)
$$ as data_type,
JSONExtract(json, data_type) as pj,
parse_data as (
	select tupleElement(pj, 'id') AS id,
		tupleElement(pj, 'name') AS name,
		tupleElement(pj, 'value') AS value,
		tupleElement(pj, 'is_active') AS is_active,
		tupleElement(pj, 'key') AS key,
		tupleElement(pj, 'list') AS list
	from json_table
),
arraySum(arrayMap(x -> toInt64(x) , list)) as avg_list_element
select floor(sum(value)) as sum_value,
	floor(avg(avg_list_element)) as sum_avg_list,
	floor(avg(toInt64(key))) as avg_key
from parse_data


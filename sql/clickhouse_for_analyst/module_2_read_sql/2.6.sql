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


--Решим задачу на агрегировании событий к большой агломерации.
--В нашем распоряжении есть таблица событий с координатами где они произошли.
--И есть вторая таблица с координатами 3 крупных городов.
--Мы бы хотели собирать статистику таким образом чтобы события произошедшие в некотором удалении от больших городов на самом деле относились к ним.
--Для примера, мы открыли приложение в 30 километрах от Москвы, и город который нам был отображен будет отличаться от Москвы, но нам не важен этот небольшой город, мы бы хотели видеть статистику именно внутри большой агломерации.
--Это зачастую важно для небольших приложений где большая часть пользователей из больших городов, и лишь небольшая часть находится за чертой.
--Ваша задача объединить данные, отфильтровать все строки где расстояние не более чем 300 км. И далее найти город который находится ближе всего к данной координате.
--Тут вам может помочь агрегирующая функция argMin
--В ответе указать сколько раз в конечной таблице встретился Выборг

with
filtered_events_data as (
    select
        l.event,
        l.long,
        l.lat,
        b.city,
        geoDistance(l.long, l.lat, b.long, b.lat) / 1000 as distance_km
    from log_json l
    	cross join big_city b
    where geoDistance(l.long, l.lat, b.long, b.lat) < 300000
),
nearest_data as (
	select
	    event,
	    argMin(city, distance_km) as nearest_city
	from filtered_events_data
	group by event
)
select countIf(nearest_city in ['Viborg']) as count_city
from nearest_data


--Предлагаю вам решить небольшую задачу по поиску расстояния между МКС (международной космической станции) и  ближайшего города.
--В первой витрине создается таблица которая при обращении отдает вам координаты МКС в текущий момент, во втором датасете лежат города с их координатами.
--Вам нужно с помощью SELECT запроса найти ближайший город над которым сейчас пролетает МКС.
--У этой задачи есть несколько вариантов решения, один из них использовать тип данных tuple для хранения координат, и с помощью функции untuple распаковать их, это позволит вам не писать 2 раза запрос к таблице с данными МКС, чтобы получить широту и долготу

with
mks_ll as (
	select  toFloat64(JSONExtractString(JSONExtractString(json, 'iss_position'), 'longitude')) AS longitude,
        toFloat64(JSONExtractString(JSONExtractString(json, 'iss_position'), 'latitude')) AS latitude
	from mks
)
select
    c.region,
    c.city,
    min(geoDistance(m.latitude, m.longitude, c.latitude, c.longitude)) / 1000 AS min_distance_km
from cities c
	cross join mks_ll m
group by c.region, c.city
order by min_distance_km asc
limit 1;
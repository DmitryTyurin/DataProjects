--Напишите запрос для нахождения номера модели, мощности двигателя и грузоподъемности для всех грузовиков стоимостью менее 3500 долларов.
--Вывести: model, engine_power и load_capacity.

select model,
	engine_power,
	load_capacity
from public.truck t
where price < 3500;


--Найдите производителей грузовиков. Вывести: maker.

select v.maker as maker
from truck t
	left join vehicle v
		using(model);


--Найдите все записи таблицы truck для грузовиков с грузоподъемностью более 1 тонны.

select *
from truck t
where load_capacity > 1;


--Для каждого производителя, выпускающего мотоциклы с весом не менее 100 кг, найти мощности двигателей таких мотоциклов.
--Вывод: производитель, мощность двигателя.

select v.maker as maker,
	m.engine_power as engine_power
from motorcycle m
	left join vehicle v using(model)
where m.weight >= 100;


--Найдите модели и цены всех имеющихся в продаже ТС (любого типа) производителя Multi.
with
all_model_data as
(
	select model, price
	from car
	union all
	select model, price
	from motorcycle
	union all
	select model, price
	from truck
)
select model, price
from all_model_data amd
	left join vehicle v using(model)
where maker = 'Multi';


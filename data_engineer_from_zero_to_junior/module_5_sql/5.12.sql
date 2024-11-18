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
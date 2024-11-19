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


--Найдите производителя, выпускающего легковые автомобили, но не грузовики.

with
truck_maker as
(
	select maker
	from vehicle
	where type = 'Truck'
)
select distinct maker
from vehicle
where type = 'Car'
	and maker not in
		(
			select maker
			from truck_maker
		);


--Найдите производителей легковых авто с мощностью двигателя не менее 700 лошадиных сил. Вывести: maker.

select v.maker as maker
from car c
	left join vehicle v using(model)
where c.engine_power > 700;


--Найдите мощности двигателей, совпадающих у двух и более мотоциклов. Вывести: engine_power.

select engine_power
from motorcycle
group by engine_power
having count(*) >= 2;


--Найдите производителей самых дешевых электрических (Electric) мотоциклов. Вывести: maker, price.

select v.maker as maker,
	m.price as price
from motorcycle m
	left join vehicle v using(model)
where m.fuel_type = 'Electric'
order by price asc
limit 1;


--Найдите производителей, которые производили бы как легковые автомобили с мощностью двигателя не менее 300 лошадиных сил,
--так и грузовики с мощностью двигателя не менее 300 лошадиных сил.
--Вывести: maker.

with
car_model as
(
	select v.maker as maker
	from car c
		left join vehicle v using(model)
	where c.engine_power >= 300
),
truck_model as
(
	select v.maker as maker
	from truck t
		left join vehicle v using(model)
	where t.engine_power >= 300
),
maker_data as
(
	select *
	from car_model
	union all
	select *
	from truck_model
)
select maker
from maker_data
group by maker
having count(*) > 1;



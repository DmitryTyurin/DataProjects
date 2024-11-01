--Посчитайте MAU за февраль 2023 года по таблице login

select toStartOfMonth(event_time) as month,
	uniqExact(uid) as MAU
from login
group by month
having month = '2023-02-01'


--Sticky Factor (Липкость) - отношение DAU/MAU то как часто пользователи заходят в приложение в течение месяца.
--Посчитайте данный показатель для month = '2023-01-01' возьмите avg от этого отношения

with
(
	select uniqExact(uid)
	from login
	where toStartOfMonth(event_time) = '2023-01-01'
) as MAU,
daily_data as (
	select
        toStartOfDay(event_time) as day,
        uniqExact(uid) as DAU,
		MAU
     from login
     where toStartOfMonth(event_time) = '2023-01-01'
     group by day
)
select
    round(avg(DAU / MAU), 4) as sticky_factor
from daily_data;


--Найдите пиковое значение(PCU) при агрегации данных по 5 минут!

with
ccu_data as (
    select toStartOfFiveMinute(event_time) as five_minutes,
        count(uid) as CCU
    from login
    group by five_minutes
    order by five_minutes
)
select max(CCU) as pcu
from ccu_data
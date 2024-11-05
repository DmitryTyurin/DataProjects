--В данном задании нужно воспользоваться запросом с прошлых шагов, применив его к данным из таблиц login (взять когорты пользователей) и finance (взять выручку).
--Далее посчитайте прогноз выручки на 100 день жизни когорты для пользователей зарегистрировавшихся: 2023-01-01
--В запросе можно использовать несколько витрин или же объединить все запросы в один большой.

with
reg_data as (
    select 'cohort 1' as cohort,
    	min(toDate(event_time)) as user_reg_date,
    	uid
    from login
    group by uid
    having user_reg_date = '2023-01-01'
),
finance_data as (
    select *
    from finance f
    	join reg_data r on f.uid = r.uid
    where is_test = 0
),
cohort_data as (
	select cohort,
		toDate(event_time) as date,
		sum(revenue_usd) as value
	from finance_data
	group by cohort, date
	order by date
)
select *
from cohort_data
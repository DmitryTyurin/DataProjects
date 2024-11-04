--Посчитайте воронку, в которой конверсия будет считаться не от общей аудитории, а из шага N в шаг N+1 по таблице funnel
--Такой метод расчета конверсии иногда используется чтобы сконцентрироваться на поведении пользователей между конкретными шагами.
--Вычислите конверсию, между level_2 и level_3

with
    uniqIf(uid, event_type = 'level_2') as level_2_users,
    uniqIf(uid, event_type = 'level_3') as level_3_users
select  round(level_3_users / level_2_users, 4)
from funnel f
where event_type in ('level_2', 'level_3')


--Посчитайте Rolling Retention 3 дня у когорты пришедшей 1 января по таблице login

with
reg_data as (
    select min(toDate(event_time)) as user_reg_date,
    	uid
    from login
    group by uid
)
select user_reg_date,
    uniq(uid) as reg_user,
    uniqIf(uid, toDate(event_time) >= user_reg_date + 3) as users_day3,
    round(users_day3 / reg_user, 4) as ret_day3
from login l
	join reg_data rd on l.uid = rd.uid
group by rd.user_reg_date
having user_reg_date = '2023-01-01';


--Посчитайте отток 3 дня у когорты пришедшей 1 января по таблице login

with
reg_data as (
    select min(toDate(event_time)) as user_reg_date,
    	uid
    from login
    group by uid
)
select user_reg_date,
    uniq(uid) as reg_user,
    uniqIf(uid, toDate(event_time) >= user_reg_date + 3) as users_day3,
    1 - round(users_day3 / reg_user, 4) as churn_day3
from login l
	join reg_data rd on l.uid = rd.uid
group by rd.user_reg_date
having user_reg_date = '2023-01-01';


--Посчитайте Накопительный ARPPU 15 дня жизни для тех кто зарегистрировался 2023-02-27.
--Уточнение, Накопительный AR PPU отличается от Накопительный AR PU тем что мы считаем только заплативших пользователей, не забудьте уточнить это в вашем запросе!
--Тестовые платежи убираем.

with
reg_data as (
    select min(toDate(event_time)) as user_reg_date,
    	uid
    from login
    group by uid
)
select user_reg_date,
  	uniq(uid) as all_users,
	sumIf(revenue_usd, toDate(event_time) <= 15 + user_reg_date) as rev_day_15,
	round(rev_day_15 / all_users, 4) as CARPU15
from finance f
	left join reg_data rd using(uid)
where 1
	and is_test = 0
	and user_reg_date = '2023-02-27'
group by user_reg_date
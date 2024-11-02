--Посчитайте воронку, в которой конверсия будет считаться не от общей аудитории, а из шага N в шаг N+1 по таблице funnel
--Такой метод расчета конверсии иногда используется чтобы сконцентрироваться на поведении пользователей между конкретными шагами.
--Вычислите конверсию, между level_2 и level_3

with
    uniqIf(uid, event_type = 'level_2') as level_2_users,
    uniqIf(uid, event_type = 'level_3') as level_3_users
select  round(level_3_users / level_2_users, 4)
from funnel f
where event_type in ('level_2', 'level_3')
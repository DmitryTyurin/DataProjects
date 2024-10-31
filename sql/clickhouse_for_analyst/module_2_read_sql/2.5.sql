--Для таблицы Титаник. Давайте посмотрим кто из пассажиров заселился в несколько номеров. Для этого
--Разобьем колонку Cabin на массив значений
--Отсортируйте по размеру массива по убыванию
--Подсказка, вам может помочь данный раздел. Например из C23 F C25 C27 получаем [23, "F", 25, 27]
--В качестве ответ впишите номер билета по которому куплено больше всего номеров.

select Ticket,
	Cabin,
	splitByChar(' ', Cabin) as tokens_cabin,
	length(tokens_cabin) as length_cabin
from titanic
group by Ticket, Cabin
order by length_cabin desc
limit 1;


--Ваша задача в этом задании заполнить данные которые пропущены, у нас есть uid (пользователь) и step_ (имя шага, события).
--Шаги помечены номерами, они соответствуют последовательности действий, то есть идут друг за другом. Но часть из них пропущена, нужно их проставить.
--Нам известно что у нас 9 пользователей, и такая последовательность шагов
--step a (1 шаг)
--step b
--step c
--step d
--step e
--step f
--step g
--step w (последний шаг)
--У каждого пользователя максимальный шаг свой! В задании не нужно использовать CROSS JOIN

with
indexOf(['step a', 'step b', 'step c', 'step d', 'step e', 'step f', 'step g', 'step w'], step) as weighted_step,
max_step as (
	select
	    UID as uid,
	    max(weighted_step) as step_
	from events
	group by UID
	order by UID
)
select sum(uid * step_) as sum_step
from max_step;


--Для таблицы Титаник, посчитайте шансы выжить для каждого пользователя исходя из его пола и класса
--Формат ответа:
--В качестве ответа впишите имя пассажира у которого шанс выжить больше всего, отсортируйте по имени если таких пассажиров несколько [A -> Z].
--Нельзя использовать JOIN Только оконные функции.

select Name,
	avg(Survived) over (partition by Sex, Pclass) as surv
from titanic
order by surv desc, Name
limit 1;


--В нашем распоряжении таблица login с логинами пользователей в наше приложение, мы снимаем лог каждые 5 минут если пользователь был в сети.
--Получается таблица примерно такого вида
+------+----------------------------+
| uid |           event_time            |
+------+----------------------------+
|    1 | 2020-10-12 20:05:00.000000 |
|    1 | 2020-10-12 20:10:00.000000 |
|    1 | 2020-10-12 20:15:00.000000 |
|    1 | 2020-10-12 20:20:00.000000 |
|------+----------------------------|
--Если разница между двумя заходами больше 5 минут, то значит пользователь начал новую сессию.
--Ваша задача разметить все сессии для каждого пользователя, то есть каждой сессии назначить номер от 1 до N
--Каждая новая сессия нового пользователя должна начинаться с 1
--В качестве ответа указать сумму по столбцу с размеченными сессиями.
--Пример корректного вывода (это пример вывода, не ориентируйтесь на сами данные):

+------+----------------------------+-----+----------+
| uid |           event_time            | ind | sessions |
+------+----------------------------+-----+----------+
|    1 | 2020-10-12 10:05:00.000000 |   1 |        1 |
|    1 | 2020-10-12 10:10:00.000000 |   0 |        1 |
|    1 | 2020-10-12 20:05:00.000000 |   1 |        2 |

with
	time_diff as (
	    select
	        id as uid,
	        date as event_time,
	        lagInFrame(event_time) over (partition by uid order by event_time) as prev_event_time
	    from login_step
	),
	ind_data as (
	    select
	        uid,
	        event_time,
	        if(prev_event_time is null or abs(dateDiff('minute', prev_event_time, event_time) > 5), 1, 0) as ind
	    from time_diff
	),
	session_data as (
	    select
	        uid,
	        event_time,
	        ind,
	        sum(ind) over (partition by uid order by event_time) as sessions
	    from ind_data
	),
	sum_data as (
		select
		    uid,
		    event_time,
		    ind,
		    sessions
		from session_data
	)
select sum(sessions) as sum_sessions
from sum_data;
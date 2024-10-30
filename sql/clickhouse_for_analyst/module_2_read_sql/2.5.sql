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



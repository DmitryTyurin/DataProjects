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



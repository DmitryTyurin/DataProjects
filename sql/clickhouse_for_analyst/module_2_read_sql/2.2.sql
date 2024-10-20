--В таблице titanic найти имя человека который
--
--Женщина
--Первый класс
--Не выжила
--В ответе указать человека с самым большим ID

select PassengerId, Name
from titanic t
where Sex = 'female'
	and Pclass = 1
	and Survived = 0
order by PassengerId desc
limit 1


--В таблице titanic найдите имя человека
--
--Который не выжил
--Отсортируйте по имени [A->Z]
--В решении использовать ORDER BY и LIMIT
--
--В качестве ответа укажите имя человека который будет на первом месте после сортировки.

select Name
from titanic t
where Survived = 0
order by Name asc
limit 1



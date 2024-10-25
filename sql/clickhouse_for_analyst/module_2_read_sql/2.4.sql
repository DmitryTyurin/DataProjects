--Ваша задача преобразовать Age в таблице Титаник с помощью функции выше и посчитать сколько будет строк с пропущенными значениями, считайте по полю Age.
--Для проверки является ли строка NULL воспользуйтесь функцией isNull(...) которая вернет только NULL строки.
--Если вы попытаетесь, посчитать таким образом count(Age) то ответом будет 0 Так как ClickHouse не берет во внимание строки с NULL значением.
--Чтобы получить корректный ответ воспользуйтесь функцией ifNull(x,alt)

with
toFloat64OrNull(Age) as age
select count(*) as count_null_age
from titanic t
where isNull(age)


--Для начала простой запрос на JOIN. У нас есть таблица с выручкой в рублях и таблица с курсом USD-RUB.
--Объедините данные и посчитайте выручку в долларах.

with
(rr.revenue_rub / ur.usdrub) as revenue_usd
select round(sum(revenue_usd)) as sum_revenue_usd
from revenue_rub rr
	join usd_rub ur using(date)


--Попрактикуемся в использовании CROSS JOIN, ваша задача реализовать столбец rank который назначает порядок числу из числового столбца, пример ниже.
--Данную задачу часто дают на собеседованиях. Решается через CROSS JOIN и GROUP BY .
--Пользоваться массивами или оконными функциями в данном задании нельзя.

with user_rank as (
	select
	    n1.user,
	    n1.value,
	    count(distinct n2.value) AS rank
	from cross_join n1
		cross join cross_join n2
	where n1.value <= n2.value
	group by  n1.user, n1.value
	order by rank
)
select sum(rank * value) as sum_rank
from user_rank;



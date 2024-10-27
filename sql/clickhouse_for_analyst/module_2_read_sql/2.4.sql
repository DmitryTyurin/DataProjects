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


--Давайте оценим как менялись глобальные продаже от года к году для приставок PS3, PS2, X360, Wii.
--Для этого нужно выполнить следующие шаги. Посчитать какие были продажи за каждый год по каждой платформе,
--отфильтровать строки с пустым значением колонки YEAR
--Затем нужно продублировать данный запрос и объединить два одинаковых запроса друг с другом, так чтобы данные за предыдущий год были в текущем. Ссылка на описание датасета.
--У вас возникнут проблемы с датой, воспользуйтесь функцией которую мы изучил ранее parseDateTimeBestEffort
--В задаче нужно использовать ASOF JOIN для объединения данных.
--Также у вас может возникнуть сложность при объединении если вы воспользуетесь таким синтаксисом using(id, dt) в данной задаче нужно использовать ASOF JOIN с таким синтаксисом ON ...=... and ... > или < ...
--Последнее условие указывает на то по какому принципу объединять данные которые не совпадают.
--После чего просто возьмите сумму от столбца разницы текущего и предыдущего года.
--У вас получится отрицательное число, впишите ответ по модулю округленный до целого числа.
--Важно, отфильтруйте все строки где предыдущий год равен 0

with current_year as (
    select
        Platform as platform,
        toYear(parseDateTime32BestEffortOrZero(Year)) AS to_year,
        sum(Global_Sales) AS cur_sale
    from video_game_sales
    where toYear(parseDateTime32BestEffortOrZero(Year)) <> 1970
    group by platform, to_year
),
previous_year as (
    select
        Platform as platform,
        toYear(parseDateTime32BestEffortOrZero(Year)) + 1 AS to_year,
        sum(Global_Sales) AS prev_sale
    from video_game_sales
    where toYear(parseDateTime32BestEffortOrZero(Year)) <> 1970
    group by platform, to_year
),
asof_join_data as (
	select
	    cy.platform,
	    cy.to_year,
	    cy.cur_sale,
	    py.prev_sale,
	    cy.cur_sale - py.prev_sale as diff
	from current_year cy
	asof left join previous_year py using(platform, to_year)
	where prev_sale > 0
	order by cy.platform, cy.to_year asc
)
select round(abs(sum(diff))) as diff
from asof_join_data
where platform in ('PS3', 'PS2', 'X360', 'Wii');





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


--В данном задании нам нужно будет вычислить вероятность выжить на Титанике для различных групп пассажиров и выяснить сколько людей из тех у кого были самые маленькие шансы на спасение в итоге выжил.
--Задание большое! Шаги которые нужно выполнить для этого:
--Для начала нужно выделить столбцы по которым будем считать вероятность выживет пассажир или нет: Pclass, Sex, Age
--Для поля Age нам нужно преобразовать тип во Float после чего заполнить пустые значения, сделать это нужно следующим способом: заполнить средним значением avg (без учета пустых значений).
--На выходе вы должны получить таблицу с такими полями: Pclass, Sex, Age, Survived
--Для поля Age воспользуйтесь функцией roundAge() для округления до различных возрастных групп
--После чего посчитайте вероятность выжить по полям Pclass, Sex, Age.  Вероятность выжить считается по формуле
--Сделайте дополнительный столбец pss в котором те у кого вероятность выжить > 0.1 называются lucky остальные именуются other (Prob > 0.1 as pss)
--Далее объедините полученные данные с таблицей Титаник чтобы выяснить какие шансы выжить есть у каждого пассажира в отдельности.
--После чего посчитайте количество other которые выжили!
--Полученное значение будет ответом

with
avg_age as (select avg(toFloat64OrNull(Age)) as average_age from titanic),
roundAge(ifNull(toFloat64OrNull(Age), (select average_age from avg_age))) as age,
countIf(Survived = 1) / count() as prob,
pss_data as (
    select  Pclass as pclass,
        Sex as sex,
        age,
        prob,
        if(prob > 0.1, 'lucky', 'other') as pss
    from titanic
    group by pclass, sex, age
),
raw_data as (
    select Name as name,
        Pclass as pclass,
        Sex as sex,
        age,
        Survived as survived
    from titanic
)
select
	rd.name,
	rd.pclass,
	rd.sex,
	rd.age,
	pd.pss,
	rd.survived
from raw_data rd
	left join pss_data pd on
	    rd.pclass = pd.pclass
	    and rd.sex = pd.sex
		and rd.age = pd.age
where rd.survived = 1 and pd.pss = 'other';






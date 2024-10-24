--В финансовом отчете Google Play есть таблица earnings она хранит список транзакций по каждой покупке, однако время и дата в данной таблице хранятся не в самом удобном виде.
--Предлагаю вам небольшую задачку на парсинг даты, вам необходимо распарсить существующую время и дату и сделать поле DateTime. PDT можно проигнорировать.
--В качестве ответа приведите transaction_id с наибольшей датой, отсортируйте в порядке убывания по дате, первая строка будет ответом.

with
replaceAll(transaction_date, ',', '') as _transaction_date,
replaceAll(transaction_time, 'PDT', '') as _transaction_time,
concat(_transaction_date, ' ', _transaction_time) as _transaction_datetime,
parseDateTimeBestEffort(_transaction_datetime) as transaction_datetime
select toDate(transaction_datetime) as date,
	toDateTime(transaction_datetime) as dt,
	transaction_id
from earnings
order by dt desc
limit 1;


--Мы с вами уже изучали функцию SUM для группировок, однако такой же функции для произведения не существует,
--вам необходимо написать скрипт который будет перемножать числа в столбце.
--Можно использовать только математические функции.
--Вам нужно вспомнить про численный тип данных и школьную математику, а точнее логарифмы.

select floor(exp(sum(log(PassengerId)))) AS product
from titanic
where PassengerId < 10;


--Посчитайте сумму продаж по Global_Sales по всем издателям, кроме топ 5 по продажам за все время .
--Задачу можно решить с помощью not in (select ... from ...) для того чтобы исключить лишних издателей.
--Для начала вам нужно найти всех издателей которые входят в топ 5 по продажам за все время, после чего исключить их из выборки и посчитать сумму по Global_Sales.

with top_5_publisher as
(
    select Publisher, sum(Global_Sales) as sum_global_sales
    from video_game_sales vgs
    group by Publisher
    order by sum_global_sales desc
limit 5
)

select floor(sum(Global_Sales)) as sum_global_sales_without_top_5
from video_game_sales vgs
where Publisher not in (select Publisher from top_5_publisher)
order by sum_global_sales_without_top_5 desc;


--Перечислите через запятую в порядке убывания: в какие годы топ 5 издателей по продажам за все время превышали продажи
--Global_Sales всех остальных более чем на 60 Ссылка на описание датасета.
--Подсказка: в комбинатор функций можно вставлять подзапросы sumIf( Global_Sales, publisher not in (SELECT ...))
--План запроса
--Первый столбец - год
--Второй - продажи топ 5 издателей
--Третий - продажи кроме топ 5 издателей
--Четвертый - посчитайте разницу между 2 и 3
--Отсортируйте результаты по годам и оставьте только те что удовлетворяют условию >60
--Годы через запятую в порядке убывания.

with top_5_publisher as
(
	select Publisher, sum(Global_Sales) as sum_global_sales
	from video_game_sales vgs
	group by Publisher
	order by sum_global_sales desc
	limit 5
)
select Year,
	sum(Global_Sales) as all_sales,
	sumIf(Global_Sales, Publisher in (select Publisher from top_5_publisher)) as top5,
	sumIf(Global_Sales, Publisher not in (select Publisher from top_5_publisher)) as not_top5,
	top5 - not_top5 as delta
from default.video_game_sales
group by Year
having delta > 60
order by Year desc;

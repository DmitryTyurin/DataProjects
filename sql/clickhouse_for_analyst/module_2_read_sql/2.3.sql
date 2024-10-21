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


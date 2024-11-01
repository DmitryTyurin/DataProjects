--Посчитайте MAU за февраль 2023 года по таблице login

select toStartOfMonth(event_time) as month,
	uniqExact(uid) as MAU
from login
group by month
having month = '2023-02-01'



--В данном задании нужно воспользоваться запросом с прошлых шагов, применив его к данным из таблиц login (взять когорты пользователей) и finance (взять выручку).
--Далее посчитайте прогноз выручки на 100 день жизни когорты для пользователей зарегистрировавшихся: 2023-01-01
--В запросе можно использовать несколько витрин или же объединить все запросы в один большой.

with
reg_data as (
    select 'cohort 1' as cohort,
    	min(toDate(event_time)) as user_reg_date,
    	uid
    from login
    group by uid
    having user_reg_date = '2023-01-01'
),
finance_data as (
    select *
    from finance f
    	join reg_data r on f.uid = r.uid
    where is_test = 0
),
cohort_data as (
	select cohort,
		toDate(event_time) as day,
		sum(revenue_usd) as value
	from finance_data
	group by cohort, day
	order by day
),
min_day as (
    select min(day) as start_date
    from cohort_data
),
all_days AS (
    select arrayJoin(arrayMap(x -> addDays(start_date, x), range(0, 100))) as day
    from min_day
),
data_ml as (
select ad.day as date,
	row_number() over() as DAY,
	if(cd.cohort = '', 'cohort 1', cd.cohort) as cohort,
	cd.value as value
from all_days ad
	left join cohort_data cd using(day)
),
predict_ml as (
select cohort,
       groupArray(DAY) as X,
       arrayCumSum(groupArray(value)) as y,
       arrayMap(x -> ln(x + 2),X) as X_ln,
       arrayReduce('simpleLinearRegression', X_ln, y) as coef,
       length(X_ln) as count_days,
       arrayMap(x -> ln(x + 2), range(length(X_ln))) as days_predict,
       tupleElement(coef, 1) as coef_a,
       tupleElement(coef, 2) as coef_b,
       arrayMap(x -> x * coef_a + coef_b, days_predict) AS array_predict
from  data_ml
group by cohort
)
select cohort,
       arrayJoin(range(count_days)) AS index_days,
       arrayElement(array_predict, index_days + 1) AS predict,
       arrayElement(y, index_days + 1) AS revenue
from predict_ml

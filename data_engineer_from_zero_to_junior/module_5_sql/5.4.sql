--Давайте найдем количество сотрудников в нашей фирме.

select count(id)
from persons;


--Давайте найдем значение максимальной зарплаты в нашей фирме.

select max(salary)
from positions;


--Давайте найдем самую высокую и самую низкую зарплату одним запросом. Результатом путь будут два столбика.

select max(salary), min(salary)
from positions;
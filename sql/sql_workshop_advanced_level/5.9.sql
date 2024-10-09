--Чтобы избежать постоянно выполняющегося объединения таблиц (JOIN) в таких запросах, было решено перенести поле is_premium_account в таблицу users.
--Требование о переносе поля реализуется в несколько шагов:
--Создать дублирующее поле is_premium_account в таблице users
--Скопировать UPDATE запросом данные этого поля из таблицы user_settings в таблицу users
--Удалить поле is_premium_account из таблицы user_settings

ALTER TABLE users ADD COLUMN is_premium_account BIT;

UPDATE users
SET is_premium_account = (
    SELECT user_settings.is_premium_account
    FROM user_settings
    WHERE user_settings.user_id = users.id
);

ALTER TABLE user_settings DROP COLUMN is_premium_account;


--Учитывая изменения в структуре данных, выполненные в предыдущей задаче, перепишите SELECT запрос:
--
--SELECT
--	users.id,
--	users.birthday,
--	user_settings.is_premium_account
--FROM users
--JOIN user_settings ON users.id = user_settings.user_id
--WHERE id = 1;
--
--
--так, чтобы он корректно исполнялся.

SELECT
	users.id,
	users.birthday,
	users.is_premium_account
FROM users
WHERE id = 1;


--Необходимо узнать: включено ли логирование медленных запросов.
--Выведите на экран значение соответствующей переменной в MySQL сервере.
--Ниакие другие строки выводить не нужно. Только одну указанную переменную.

SHOW VARIABLES LIKE 'slow_query_log';


--Необходимо узнать расположение файла с логами медленных запросов.
--Выведите на экран значение соответствующей переменной в MySQL сервере.
--Ниакие другие строки выводить не нужно. Только одну указанную переменную.

SELECT @@slow_query_log_file;


--Необходимо узнать критерий для медленных запросов (время исполнения в секундах).
--Выведите на экран значение соответствующей переменной в MySQL сервере.
--Ниакие другие строки выводить не нужно. Только одну указанную переменную.

SELECT @@long_query_time;


--Необходимо узнать: включеншо ли логирование для запросов, не использующих индексы.
--Выведите на экран значение соответствующей переменной в MySQL сервере.
--Ниакие другие строки выводить не нужно. Только одну указанную переменную.

SELECT @@log_queries_not_using_indexes;


--Необходимо решить данную проблему, т.к. такие запросы исполняются медленно и создают нагрузку на сервер.
--Напишите код, который устранит появление указанных SELECT запросов в логах.

ALTER TABLE users
ADD INDEX idx_users_email (email);


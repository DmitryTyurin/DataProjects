--Выведите все записи из таблицы channels, у которых в поле title встречается слово 'sql'.
--Отсортируйте выборку по полю title.
--В результате необходимо оставить только следующие поля: идентификатор канала, название канала

select id, title
from channels
where title like '%sql%'
order by title asc


--Принято решение расширить возможности поиска по названиям каналов.
--Добавьте полнотекстовый индекс на поле title таблицы channels.

create fulltext index title_idx on channels(title)


--Используя полнотекстовый поиск, выведите все записи из таблицы channels, у которых в поле title встречается слово 'sql', но не встречается 'server'.
--Отсортируйте выборку по полю title.
--В результате необходимо оставить только следующие поля: идентификатор канала, название канала

select id, title
from channels
where match(title) against('+sql -server' in boolean mode)
order by title


--Создайте представление v_users_without_phone (название важно для проверки!),
--которое выводит все поля таблицы users и содержит только те строки, в которых не указан телефон (поле phone пустое).

create view v_users_without_phone as
(
    select *
    from users
    where phone is null
);


--Оказалось, что данных из таблицы users недостаточно в нашем представлении. Остальные данные о пользователях находятся в таблице user_settings. Необходимо ее присоединить (операцией INNER JOIN) к общей выборке.
--Одной командой (!) пересоздайте представление v_users_without_phone из прошлого задания, присоединив по внешнему ключу к общей выборке таблицу user_settings.
--Выводить необходимо также все поля общей выборки (можно звездочкой).
--Также необходимо поменять условие фильтрации: теперь нас интересуют пользователи, у которых указана дата рождения (в поле birthday есть какое-то значение).

create or replace view v_users_without_phone as
(
    select *
    from users u
    inner join user_settings us on us.user_id = u.id
    where u.birthday is not null
);


--Отлично, у нас есть работающее представление v_users_without_phone.
--Теперь нужно с его помощью получить список пользователей, у которых в приложении установлен русский язык (поле app_language в соответствующем значении).
--Вывести необходимо только следующие поля: идентификатор пользователя, email пользователя
--Отсортировать выборку по полю email.

select id, email
from v_users_without_phone
where app_language = 'russian'
order by email


--Принято решение удалить представление v_users_without_phone.
--Напишите соответствующий запрос. При удалении необходимо выполнить проверку существования данного представления на сервере.

drop view if exists v_users_without_phone


--В таблицах сообщений (saved_messages, private_messages,) появляются записи с пустым полем body (сообщения без текста). Решено удалять такие сообщения процедурой.
--Напишите хранимую процедуру с названием remove_empty_messages (название важно для проверки!), которая удаляет все строки из указанных таблиц, у которых в поле body отсутствует значение (NULL).

CREATE PROCEDURE remove_empty_messages()
BEGIN
    DELETE FROM saved_messages WHERE body IS NULL;
    DELETE FROM private_messages WHERE body IS NULL;
END


--К хранимой процедуре из предыдущего задания необходимо добавить очистку еще 2 таблиц: channel_messages, group_messages.
--В итоге очищать нужно "пустые сообщения" из 4 таблиц: saved_messages, private_messages, channel_messages, group_messages.
--Перепишите хранимую процедуру с названием remove_empty_messages, которая удаляет все строки из указанных таблиц, у которых в поле body отсутствует значение (NULL).

DROP PROCEDURE IF EXISTS remove_empty_messages;

CREATE PROCEDURE remove_empty_messages()
BEGIN
    DELETE FROM saved_messages WHERE body IS NULL;
    DELETE FROM private_messages WHERE body IS NULL;
    DELETE FROM channel_messages WHERE body IS NULL;
    DELETE FROM group_messages WHERE body IS NULL;
END


--Вызовите процедуру remove_empty_messages.

CALL remove_empty_messages();


--Решено снова изменить логику работы процедуры remove_empty_messages. Теперь она должна удалять "пустые сообщения"  конкретного пользователя (отправителя сообщения).
--Идентификатор пользователя (user_number) должен передаваться в процедуру в качестве параметра с типом данных BIGINT UNSIGNED.
--Перепишите соответствующим образом хранимую процедуру, чтобы она принимала параметр user_number и удаляла из всех таблиц сообщений (saved_messages, private_messages, channel_messages, group_messages) записи указанного пользователя, у которых  в поле body отсутствует значение (NULL).

DROP PROCEDURE IF EXISTS remove_empty_messages;

CREATE PROCEDURE remove_empty_messages(
IN user_number BIGINT UNSIGNED
)
BEGIN
    DELETE FROM saved_messages
        WHERE user_id = user_number AND body IS NULL;
    DELETE FROM private_messages
        WHERE sender_id = user_number AND body IS NULL;
    DELETE FROM channel_messages
        WHERE sender_id = user_number AND  body IS NULL;
    DELETE FROM group_messages
        WHERE sender_id = user_number AND  body IS NULL;
END


--Напишите код, удаляющий процедуру с именем remove_empty_messages. Не забудьте проверку на существование.

DROP PROCEDURE IF EXISTS remove_empty_messages;



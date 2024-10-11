--Необходимо удалить канал номер 1 из таблицы channels:
--
--CREATE TABLE channels (
--	id SERIAL, # идентификатор канала
--	title VARCHAR(45),
--	icon VARCHAR(45),
--	invite_link VARCHAR(100),
--	settings JSON,
--	owner_user_id BIGINT UNSIGNED NOT NULL,
--	is_private BIT,
--  	created_at DATETIME DEFAULT NOW(),
--
--  	FOREIGN KEY (owner_user_id) REFERENCES users (id)
--);
--
--Но его удаление напрямую вызывает ошибку при проверке внешних ключей:
--Действительно, у канала есть подписчики (записи в таблице channel_subscribers):
--
--CREATE TABLE channel_subscribers (
--  	channel_id BIGINT UNSIGNED NOT NULL, # ссылка на номер канала
--  	user_id BIGINT UNSIGNED NOT NULL,
--  	status ENUM('requested', 'joined', 'left'),
--  	created_at DATETIME DEFAULT NOW(),
--  	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
--
--  	FOREIGN KEY (user_id) REFERENCES users (id),
--  	FOREIGN KEY (channel_id) REFERENCES channels (id)
--);
--
--И также в канале есть сообщения (записи в таблице channel_messages):
--
--CREATE TABLE channel_messages (
--	id SERIAL,
--	channel_id BIGINT UNSIGNED NOT NULL, # ссылка на номер канала
--	sender_id BIGINT UNSIGNED NOT NULL,
--	media_type ENUM('text', 'image', 'audio', 'video'),
--	body text,
--	filename VARCHAR(100) NULL,
--	created_at DATETIME DEFAULT NOW(),
--
--	FOREIGN KEY (sender_id) REFERENCES users (id),
--	FOREIGN KEY (channel_id) REFERENCES `channels` (id)
--);
--Таким образом, чтобы удалить канал номер 1, сначала необходимо удалить соответствующие записи в зависимых таблицах.
--Также очевидно, что данная операция является одним элементом бизнес логики приложения. Соответственно, ее необходимо выполнить в транзакции.
--Напишите SQL код, который в транзакции удаляет канал номер 1, все сообщения в нем и информацию о его подписчиках.
--Подсказка
--Порядок удаления строк в разных таблицах важен, иначе код не будет работать.

START TRANSACTION;

DELETE FROM channel_messages WHERE channel_id = 1;
DELETE FROM channel_subscribers WHERE channel_id = 1;
DELETE FROM channels WHERE id = 1;

COMMIT;


--По аналогии с предыдущим заданием напишите SQL код, который в транзакции удаляет канал номер 1, все сообщения в нем и информацию о его подписчиках.
--Но в этот раз транзакцию необходимо откатить назад (не фиксировать).

START TRANSACTION;

DELETE FROM channel_messages WHERE channel_id = 1;
DELETE FROM channel_subscribers WHERE channel_id = 1;
DELETE FROM channels WHERE id = 1;

ROLLBACK;


--Теперь оберните код написанной транзакции (с коммитом) в процедуру.
--Напишите процедуру с названием remove_channel (название важно для проверки!), которая будет выполнять код из первого задания.
--Подсказка
--Код должен содержать несколько команд.
--Предварительно удалите существующую процедуру с проверкой
--После этого добавьте имеющийся код в процедуру
--Внимательно читайте текст ошибок

DROP PROCEDURE IF EXISTS remove_channel;

DELIMITER //

CREATE PROCEDURE remove_channel()
BEGIN
    START TRANSACTION;

    DELETE FROM channel_messages WHERE channel_id = 1;
    DELETE FROM channel_subscribers WHERE channel_id = 1;
    DELETE FROM channels WHERE id = 1;

    COMMIT;
END //

DELIMITER ;


--Развиваем нашу процедуру remove_channel дальше. Теперь она должна принимать в качестве параметра номер канала, который должен удаляться.
--Перепишите соответствующим образом код создания процедуры remove_channel, чтобы она принимала параметр channel_number и удаляла записи из таблиц channel_subscribers, channel_messages, channels, учитывая номер переданного канала.
--Важно! Подумайте над типом данных передаваемого параметра (номер канала) с учетом определения таблицы

DROP PROCEDURE IF EXISTS remove_channel;

DELIMITER //

CREATE PROCEDURE remove_channel(IN channel_number BIGINT UNSIGNED)
BEGIN
    START TRANSACTION;

    DELETE FROM channel_messages WHERE channel_id = 1;
    DELETE FROM channel_subscribers WHERE channel_id = 1;
    DELETE FROM channels WHERE id = 1;

    COMMIT;
END //

DELIMITER ;


--Теперь вызовите процедуру remove_channel на исполнение, передав в нее номер канала = 1.

CALL remove_channel(1);


-- Выведите информацию о текущем уровне изоляции транзакций на сервере.

SELECT @@transaction_ISOLATION;


--Установите для своей сессии уровень изоляции транзакций, устраняющий проблему фантомного чтения.

SET SESSION TRANSACTION ISOLATION LEVEL SERIALIZABLE;


-- Установите для своей сессии уровень изоляции транзакций, устраняющий только проблему грязного чтения, но не слишком избыточный.

SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;


--Заблокируйте таблицу пользователей на чтение, затем выведите количество строк в ней и после этого разблокируйте таблицу.

LOCK TABLES users READ;
SELECT COUNT(*) FROM users;
UNLOCK TABLES;



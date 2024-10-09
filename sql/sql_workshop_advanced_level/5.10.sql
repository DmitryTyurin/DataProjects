--В логах проблемных запросов обнаружен следующий SELECT запрос:
--
--SELECT *
--FROM channels c
--JOIN channel_messages cm ON c.id = cm.channel_id
--JOIN channel_message_reactions cmr ON cm.id = cmr.message_id
--JOIN reactions_list rl ON rl.id = cmr.reaction_id
--JOIN users u ON u.id = cm.sender_id
--WHERE c.id = 1
--
--
--Необходимо найти в нем узкое место (пробемную таблицу). Для этого получите план исполнения этого запроса.

EXPLAIN SELECT *
...


--SELECT *
--FROM channels AS c
--JOIN channel_messages AS cm ON c.id = cm.channel_id
--JOIN channel_message_reactions AS cmr ON cm.id = cmr.message_id
--JOIN reactions_list AS rl ON rl.id = cmr.reaction_id
--JOIN users AS u ON u.id = cm.sender_id
--WHERE c.id = 1
--
--Исходя из этой информации, определите проблемную таблицу и верните ей внешний ключ.
--Напишите SQL-запрос, добавляющий недостающий внешний ключ нужной таблице

ALTER TABLE channel_message_reactions
ADD FOREIGN KEY (message_id) REFERENCES channel_messages(id);
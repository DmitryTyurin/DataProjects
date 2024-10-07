--Поступила задача: сделать неактивными (is_active = false) всех несовершеннолетних пользователей. Решить ее необходимо с помощью функции.
--Требования к функции:
--Название: deactivate_infants
--Возвращаемый тип данных: INT
--Функция должна вернуть количество записей, которые она обновила (системная фунция ROW_COUNT() в помощь)

CREATE FUNCTION deactivate_infants() RETURNS INT
MODIFIES SQL DATA
BEGIN
    UPDATE users
    SET is_active = 0
    WHERE (YEAR(NOW()) - YEAR(birthday)) < 18;
    RETURN ROW_COUNT();
END;


--Вызовите функцию deactivate_infants.

SELECT deactivate_infants();


--Нашу функцию deactivate_infants необходимо доработать. А именно: деактивировать несовершеннолетние аккаунты только в случае, если они бесплатные.
--Код должен содержать несколько команд.
--Предварительно удалите существующую функцию с проверкой
--Деактивируйте учетные записи только если возраст < 18 и is_premium_account = false
--Для получения нужных строк используйте конструкцию UPDATE-JOIN
--Функция должна вернуть количество записей, которые она обновила (системная функция ROW_COUNT() в помощь)

DROP FUNCTION IF EXISTS deactivate_infants;

CREATE FUNCTION deactivate_infants() RETURNS INT
MODIFIES SQL DATA
BEGIN
    DECLARE result INT DEFAULT 0;

    UPDATE users u
    INNER JOIN user_settings us ON u.id = us.user_id
    SET u.is_active = 0
    WHERE us.is_premium_account = false AND (YEAR(NOW()) - YEAR(u.birthday)) < 18;

    SELECT COUNT(*) INTO result FROM users u
    WHERE u.is_active = 0;

    SET result = ROW_COUNT();

    RETURN result;
END;


--Принято решение внедрить параметры в написанную ранее функцию deactivate_infants и изменить логику ее работы.
--Новые принимаемые параметры:
--deact_infants (тип BIT) - деактиваровать несовершеннолетних
--deact_free_accounts (тип BIT) - деактиваровать бессплатные аккаунты
--Перешишите функцию в соответствии с новой логикой и новыми параметрами.
--Деактиваровать несовершеннолетних только если параметр deact_infants = 1.
--Деактиваровать бессплатные аккаунты только если параметр deact_free_accounts = 1.
--Функция должна возвращать суммарное количество удаленных записей.
--Подсказка
--Код должен содержать несколько команд.
--Предварительно удалите существующую функцию с проверкой
--Удобнее всего сделать несколько отдельных UPDATE запросов в функции
--Заведите переменную, в которую будете суммировать удаленные записи из отдельных запросов

DROP FUNCTION IF EXISTS deactivate_infants;

CREATE FUNCTION deactivate_infants(
    deact_infants BIT,
    deact_free_accounts BIT
)
RETURNS INT READS SQL DATA
BEGIN
    DECLARE result_1 INT DEFAULT 0;
    DECLARE result_2 INT DEFAULT 0;

    IF deact_infants = 1 THEN
        UPDATE users
        SET is_active = 0
        WHERE YEAR(NOW()) - YEAR(birthday) < 18;

        SET result_1 = ROW_COUNT();
    END IF;

    IF deact_free_accounts = 1 THEN
        UPDATE users u
        INNER JOIN user_settings us ON u.id = us.user_id
        SET u.is_active = 0
        WHERE us.is_premium_account = false;

        SET result_2 = ROW_COUNT();
    END IF;


    RETURN result_1 + result_2;

END;


--Напишите код, удаляющий функцию с именем deactivate_infants . Не забудьте проверку на существование.

DROP FUNCTION IF EXISTS deactivate_infants;


--В MySQL сервере есть глобальная переменная, которая позволяет включить или выключить проверку внешних ключей.
--Выведите текущее значение этой переменной.

SHOW VARIABLES LIKE 'foreign_key_checks';


--Предварительно отключить проверку внешних ключей
--Исполнить приведенный фрагмент дампа (чтобы он смог успешно создать обе таблицы и добаить 5 записей в таблицу user_settings)
--Включить проверку внешних ключей

SET FOREIGN_KEY_CHECKS = 0;
....
SET FOREIGN_KEY_CHECKS = 1;


--Объявите пользовательскую переменную user_stories_count, сохраните в нее количество записей в таблице stories, которые относятся к пользователю номер 1 (поле user_id определяет автора истории).
--После этого выведите значение переменной с помощью SELECT запроса.
--Придется исполнить несколько команд:
--Сначала объявите пользовательскую переменную
--Затем присвойте ей значение из запроса
--И верните значение переменной на экран

SET @user_stories_count = (
    SELECT COUNT(*)
    FROM stories
    WHERE user_id = 1
);

SELECT @user_stories_count AS user_stories_count;


--Необходимо написать триггер, который при удалении строки из таблицы users, создает запись об этом событии в таблице logs.

CREATE TRIGGER trigger_delete_user
AFTER DELETE ON users
FOR EACH ROW
BEGIN
    INSERT INTO logs (value)
    VALUES ('Удалена строка из таблицы пользователей.');
END;


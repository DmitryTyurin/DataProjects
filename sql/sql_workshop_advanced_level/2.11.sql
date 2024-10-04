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


Нашу функцию deactivate_infants необходимо доработать. А именно: деактивировать несовершеннолетние аккаунты только в случае, если они бесплатные.
Код должен содержать несколько команд.
Предварительно удалите существующую функцию с проверкой
Деактивируйте учетные записи только если возраст < 18 и is_premium_account = false
Для получения нужных строк используйте конструкцию UPDATE-JOIN
Функция должна вернуть количество записей, которые она обновила (системная функция ROW_COUNT() в помощь)

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

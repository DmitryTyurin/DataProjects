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


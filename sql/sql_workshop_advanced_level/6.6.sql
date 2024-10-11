--Необходимо узнать: включено ли  общее логирование.
--Выведите на экран значение соответствующей переменной в MySQL сервере.
--Ниакие другие строки выводить не нужно. Только одну указанную переменную.

select @@general_log;


--Необходимо узнать расположение файла с общими логами.
--Выведите на экран значение соответствующей переменной в MySQL сервере.
--Ниакие другие строки выводить не нужно. Только одну указанную переменную.

select @@general_log_file;


--Напишите функцию get_factorial_func (название важно для проверки!), которая в цикле REPEAT - UNTIL вычисляет факториал заданного числа.
--Требования к функции:
--название get_factorial_func
--принимает целое число в качестве параметра
--использует именно цикл REPEAT - UNTIL
--возвращает целое число, равное факториалу переданного числа в параметре
--Подсказка
--Код должен содержать несколько команд.
--Предварительно удалите существующую функцию с проверкой
--После этого добавьте имеющийся код в функцию
--Внимательно читайте текст ошибок
--Тип функции: DETERMINISTIC

DROP FUNCTION IF EXISTS get_factorial_func;

DELIMITER //

CREATE FUNCTION get_factorial_func(n INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE result INT DEFAULT 1;

    IF n < 0 THEN
        RETURN NULL;
    END IF;
    REPEAT
        IF n <= 1 THEN
            SET result := 1;
        END IF;
        SET result := result * n;
        SET n := n - 1;
    UNTIL n <= 1
    END REPEAT;

    RETURN result;
END //

DELIMITER ;


--Напишите процедуру get_factorial_proc (название важно для проверки!), которая в цикле WHILE вычисляет факториал заданного числа.
--Требования к процедуре:
--название get_factorial_proc
--принимает целое число в качестве параметра
--использует именно цикл WHILE
--выводит целое число, равное факториалу переданного числа в параметре

DELIMITER //

CREATE PROCEDURE get_factorial_proc(IN num INT)
BEGIN
    DECLARE factorial INT DEFAULT 1;
    DECLARE counter INT DEFAULT 1;

    WHILE counter <= num DO
        SET factorial = factorial * counter;
        SET counter = counter + 1;
    END WHILE;

    SELECT factorial;
END //

DELIMITER ;


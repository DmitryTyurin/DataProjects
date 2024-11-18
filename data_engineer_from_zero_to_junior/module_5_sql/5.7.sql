--Напишите запрос для получения уникальных значений в столбцах c из таблиц a и b, используя UNION или UNION ALL.

select c
    from a
union
select c
    from b;
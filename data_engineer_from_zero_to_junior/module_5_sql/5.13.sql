CREATE TABLE first_names (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL
);

CREATE TABLE middle_names (
    id SERIAL PRIMARY KEY,
    middle_name VARCHAR(50) NOT NULL
);

CREATE TABLE last_names (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(50) NOT NULL
);


INSERT INTO first_names (first_name) VALUES ('Иван'), ('Петр'), ('Сидор');
INSERT INTO middle_names (middle_name) VALUES ('Иванович'), ('Петрович'), ('Сидорович');
INSERT INTO last_names (last_name) VALUES ('Иванов'), ('Петров'), ('Сидоров');


SELECT t1.first_name || ' ' || t2.middle_name || ' ' || t3.last_name AS full_name
FROM first_names t1
    join middle_names t2
        on t1.id = t2.id
    join last_names
        t3 on t2.id = t3.id
ORDER BY full_name desc;
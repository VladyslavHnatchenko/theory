CREATE TABLE table_name (
    id INTEGER,
    name VARCHAR,
    make VARCHAR,
    model VARCHAR,
    year DATE,
    PRIMARY KEY (id)
);


INSERT INTO table_name (id, name, make, model, year)
VALUES (1, 'Marly', 'Ford', 'Explorer', '2000');


UPDATE table_name
SET name='Chevrolet'
WHERE id=1;


SELECT name, make, model
FROM table_name;


SELECT * FROM table_name;


SELECT name, make, model
FROM table_name
WHERE year >= '2000-01-01' AND year <= '2006-01-01';


DELETE FROM table_name
WHERE name='Ford';


DROP TABLE table_name;

SELECT 10 + 20;
SELECT 10 * 20;
SELECT 100 / 20;

CREATE TABLE employees (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  salary INT,
);

insert into employees values(1,'james',2000);
insert into employees values(2,'Carmen',4000);
insert into employees values(2,'Charles',1000);

select salary + 500 from employees;
select salary + 500 from employees where salary < 3000;

SELECT * FROM employees
ORDER BY salary;

SELECT * FROM employees
ORDER BY salary DESC;

SELECT DISTINCT salary
FROM employees;

CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  gender TEXT NOT NULL
);

INSERT INTO students VALUES (1, 'Ryan', 'M');
INSERT INTO students VALUES (2, 'Joanna', 'F');

ALTER TABLE students ADD(grade TEXT);
ALTER TABLE students MODIFY grade INTEGER;

SELECT name FROM students;

UPDATE students
set grade = 10
WHERE id = 1;

UPDATE students
set grade = 8
WHERE id = 2;

SELECT id,name,gender,grade FROM students

DELETE FROM students WHERE grade=8
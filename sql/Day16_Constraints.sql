--Enforce non-null email.

ALTER TABLE employees
ALTER COLUMN email SET NOT NULL;

--check constraints to avoid empty strings
ALTER TABLE employees
ADD CONSTRAINT email_not_empty CHECK (email <> '');

--unique constraint to avaoid duplicate email
ALTER TABLE employees
ADD CONSTRAINT unique_email UNIQUE (email);


--Make phone unique.
ALTER TABLE customers
ADD COLUMN phone_number VARCHAR(20);

ALTER TABLE customers 
ADD CONSTRAINT unique_phone_number unique(phone_number)


SELECT email, COUNT(*) 
FROM employees
GROUP BY email
HAVING COUNT(*) > 1;


SELECT * 
FROM employees
WHERE email = 'unknown@example.com';

update employees 
set email ='priya@abc.com'
where id=4


--Set default join date.

ALTER TABLE customers
ADD COLUMN join_date date

alter table customers
alter column join_date set default '01-01-2020'

update customers
set join_date = '01-01-2020'
where join_date is NULL

update customers
set phone_number = '1234567896'
where customer_id = 1

select * from employees

--Prevent negative salary.

ALTER TABLE employees
ADD CONSTRAINT salary_non_negative CHECK (salary >= 0);

update employees
set  salary = -65000
where id = 4
ERROR: new row for relation "employees" violates check constraint "salary_non_negative"


--Add check constraint to age.
alter table employees
add column age int

alter table employees
add constraint age_non_negative CHECK (age >=0)

update employees 
set age = 20
where age is null

update employees
set age = -20
where id =1
ERROR: new row for relation "employees" violates check constraint "age_non_negative"
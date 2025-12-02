select * from employees;

select name from employees where email is null;

update employees set salary = '3000' where salary is null


select count(*) as null_salaries from employees where salary is null

select name,department from employees where email is not null
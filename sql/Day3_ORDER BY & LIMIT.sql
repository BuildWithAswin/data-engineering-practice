select name,salary from employees where id <= 5 order by salary desc 

select name,salary from employees where id <= 5 order by salary desc limit 3;

select name,salary from employees where id <=3 order by salary asc;


select name,salary from employees order by salary asc limit 3;

select name ,department from employees order by name asc;

select name,salary from employees  order by salary desc offset 1 limit 1

select id,name from employees order by id desc limit 5
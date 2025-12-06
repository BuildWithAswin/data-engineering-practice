select * from employees;
select * from department;




select department,count(department) as empl_count from employees group by department order by empl_count desc limit 1;

select name,department, salary as avg_non_hr_salary from employees where department <> 'HR' group by department;


select name,department, salary as salary_above_com_avg from employees where 
salary > (select avg(salary) from employees);


select name,department from employees where email is null;


select c.customer_id,c.customer_name,o.order_id,o.order_date
from customers c
INNER JOIN orders o 
ON c.customer_id = o.customer_id;
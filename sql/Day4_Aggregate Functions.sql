select count(*) from employees;

select sum(salary) from employees;

select round(avg(salary), 2) as avg_salary from employees;

select round(avg(salary), 2) as hr_avg_salary from employees where department='HR';

select department,round(avg(salary), 2) as avg_salary from employees group by department;

select department,round(avg(salary)) as avg_salary from employees group by department having avg(salary) > 60000;


select department,count(*) as emp_count from employees group by department having count(*) > 2 

select department, min(salary) from employees group by department;

select department, max(salary) from employees group by department;

select * from employees;
select count(*) as sales_employee_count from employees where department='Sales';
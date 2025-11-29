select * from employees;

select department,sum(salary) as total_salary from employees group by department order by total_salary desc;

select department,round(avg(salary)) as avg_salary from employees group by department order by avg_salary;

select department,round(avg(salary)) as avg_salary from employees group by department having avg(salary) > 60000;

select city,count(name) as no_employees from employees group by city;

select department,name,max(salary) as max_salary from employees group by department;




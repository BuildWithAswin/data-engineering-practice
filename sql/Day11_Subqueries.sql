--Employees earning above average.
select e.name,e.department,e.salary 
from employees e 
where e.salary > (select avg(e.salary) from employees e)
order by e.salary desc 

--Employees earning above department average.
select e.name,e.department,e.salary 
from employees e
where e.salary > 
(select round(avg(e2.salary)) avg_salary_per_dept
from employees e2 where e2.department = e.department)
order by e.salary desc 

--Second highest salary using subquery.(per dept)
select e.name,e.department,e.salary as second_highest
from employees e 
where e.salary = 
(select e2.salary from employees e2 where e2.department = e.department
order by e2.salary desc limit 1 offset 1)
order by e.salary desc 

--Top 3 salaries in each department

select e1.name,e1.salary,e1.department from 
employees e1 where 3 > (
select count(distinct(e2.salary))
from employees e2 
where e2.department = e1.department
and e2.salary > e1.salary
)
order by e1.department, e1.salary desc 

--Products with price higher than category average.

select p.category,p.product_name,p.price
from products p
where p.price > (select round(avg(p2.price)) 
from products p2
where p.category = p2.category)
order by p.category,p.price desc 

--Customers with no purchases.
select c.customer_name,o.order_id from
customers c 
LEFT JOIN orders o on o.customer_id = c.customer_id 
where o.order_id is NULL 

--Latest order per customer.
select c.customer_name,o.order_date 
from customers c
JOIN orders o on o.customer_id = c.customer_id
where o.order_date = (select MAX(o2.order_date) 
from orders o2
where o.customer_id = o2.customer_id)
order by order_date desc 





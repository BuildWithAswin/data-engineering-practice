--Rank customers by total spending

select c.customer_name,sum(o.total_amount) as total_spent,
RANK() OVER (
    ORDER BY sum(o.total_amount) DESC 
) AS spend_rank 
from customers c
JOIN orders o on o.customer_id = c.customer_id
group by c.customer_name
order by customer_name asc 

--Running total of a customer's spending over time

select c.customer_id,c.customer_name,o.order_date,o.total_amount,
sum(total_amount) OVER (PARTITION BY c.customer_id order by order_date) AS running_total
from customers c 
JOIN orders o on o.customer_id = c.customer_id

order by c.customer_name,o.order_date asc 

--Get previous order amount (LAG)

select c.customer_id, c.customer_name,o.order_date,o.total_amount,
LAG(o.total_amount) OVER (
    PARTITION BY c.customer_id order by o.order_date
    ) AS previous_order_amount
from customers c 
JOIN orders o on o.customer_id = c.customer_id
order by c.customer_id,o.order_date

--Find most popular products using DENSE_RANK
select p.product_name,SUM(oi.quantity) AS total_sold,
DENSE_RANK() OVER (ORDER BY SUM(oi.quantity) DESC) AS popularity_rank
from order_items oi 
JOIN products p on p.product_id = oi.product_id
group by p.product_name


--Find most popular products in each category using DENSE_RANK
select p.category,p.product_id,p.product_name,SUM(oi.quantity) AS total_sold,
DENSE_RANK() OVER (PARTITION BY p.category ORDER BY SUM(oi.quantity) DESC) AS popularity_rank
from order_items oi 
JOIN products p on p.product_id = oi.product_id
group by p.category,p.product_id,p.product_name

--Most expensive order per customer (RANK + PARTITION)
select c.customer_id,c.customer_name,o.total_amount,o.total_amount as top_orders,
DENSE_RANK() OVER (PARTITION BY c.customer_id order by o.total_amount desc)  as order_rank
from customers c
JOIN orders o on o.customer_id = c.customer_id 
order by customer_id, order_rank
 

--Compute percent contribution of each order to total sales
select o.order_id,o.customer_id,o.total_amount,
round(o.total_amount * 100.0 / sum(o.total_amount)  OVER (),2) AS percent_of_total_sales
from orders o
order by percent_of_total_sales desc 

--Rank employees by salary.
select e.name,e.salary,
RANK() OVER(order by e.salary desc) AS salary_rank
from employees e


--Running total of daily sales.
select o.order_date,o.total_amount,
sum(o.total_amount) over(order by o.order_date) as running_total
from orders o
order by o.order_date asc

--Top 3 customers per month.
select c.customer_id,c.customer_name,o.order_date,o.total_amount
from customers c
JOIN orders o on o.customer_id = c.customer_id
order by o.order_date,o.total_amount desc 

--Lag previous order amount.
select c.customer_id,
       c.customer_name,
       o.order_date,
       o.total_amount,
LAG(o.total_amount) 
OVER(PARTITION BY c.customer_id order by o.order_date) AS previous_amount
from customers c 
JOIN orders o on o.customer_id = c.customer_id
order by c.customer_name,o.order_date asc



--Lead next salary value.
select e.name,e.salary,
LEAD(e.salary) OVER(order by e.salary)  as next_salary
from employees e 


--Find customers who placed orders in 2024 but not in 2025.
select distinct c.customer_name
from customers c 
JOIN orders o2024 on c.customer_id = o2024.customer_id
where EXTRACT(YEAR from o2024.order_date ) = 2024
AND NOT EXISTS (
    select 1  
    from orders o2025
    where  c.customer_id = o2025.customer_id
    AND EXTRACT(YEAR from o2025.order_date ) = 2025
    )



--Find products that were never ordered.
select p.product_name 
from products p 
LEFT JOIN order_items oi on oi.product_id = p.product_id
where oi.product_id IS NULL

--Find the second highest order value.
select distinct total_amount as second_highest_order
from orders
order by total_amount desc 
limit 1 offset 1

--Find employees who do not have a manager.
select name
from employees 
where manager is null


--Classify salary as High / Medium / Low.
select e.name,e.salary,
CASE 
    WHEN e.salary <  20000 THEN 'LOW'
    WHEN e.salary BETWEEN 20000 AND 49999 THEN 'MEDIUM'
    ELSE 'HIGH'
END AS salary_category
from employees e 
order by e.salary desc 


--Mark customers as VIP or Regular.
select c.customer_name, SUM(p.price * oi.quantity) as total_spent,
CASE
    WHEN SUM(p.price * oi.quantity) > 50000 THEN 'VIP'
    ELSE 'REGULAR'
END AS category 
from customers c 
JOIN orders o on c.customer_id = o.customer_id 
JOIN order_items oi on oi.order_id = o.order_id
JOIN products p on p.product_id = oi.product_id
group by c.customer_name
order by total_spent desc 


--Categorize orders by value.
select o.order_id, o.total_amount,
CASE 
    WHEN o.total_amount >= 50000 THEN 'HIGH'
    WHEN o.total_amount BETWEEN 20000 and 49999 THEN 'MEDIUM'
    ELSE 'LOW'
END AS value 
from orders o 
order by o.total_amount desc 


--adding boolean field to orders table and updating value 

ALTER TABLE orders
ADD COLUMN is_delivered BOOLEAN;

UPDATE orders 
SET is_delivered = FALSE
WHERE order_id IN (1,4,6,7);

--Convert boolean flags to status text.
select o.order_id, o.is_delivered,
CASE 
    WHEN o.is_delivered = FALSE THEN 'NOT DELIVERED'
    ELSE 'DELIVERED'
END AS STATUS
from orders o

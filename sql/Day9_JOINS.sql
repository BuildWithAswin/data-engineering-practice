--List customers with their orders.
select c.customer_name,c.customer_id, o.order_id, oi.order_id, p.product_name
from customers c
INNER JOIN orders o on c.customer_id = o.customer_id
INNER JOIN order_items oi on o.order_id = oi.order_id
INNER JOIN products p on oi.product_id = p.product_id

--Find customers without orders.
select c.customer_id,c.customer_name,o.order_id
from customers c 
LEFT JOIN orders o on c.customer_id = o.customer_id
where o.order_id IS NULL

--Find orders without customers
select c.customer_id,c.customer_name, o.order_id 
from customers c
RIGHT JOIN  orders o on c.customer_id = o.customer_id
where c.customer_id is NULL


--Count orders per customer.
select c.customer_id,c.customer_name,count(o.order_id) as no_of_orders
from customers c 
LEFT JOIN orders o on c.customer_id = o.customer_id
group by c.customer_id,c.customer_name
order by no_of_orders desc 

--Show customer name with total order amount.
select c.customer_id,c.customer_name,sum(o.total_amount) as total_order_amount
from customers c 
LEFT JOIN orders o on c.customer_id = o.customer_id
group by c.customer_id,c.customer_name 
order by total_order_amount desc 


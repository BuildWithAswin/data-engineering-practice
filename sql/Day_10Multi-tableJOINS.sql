--Join customers → orders → products.

select c.customer_name,c.city,o.order_date,oi.quantity,p.product_name 
from customers c
JOIN orders o on o.customer_id = c.customer_id
JOIN order_items oi on oi.order_id = o.order_id
JOIN products p on p.product_id = oi.product_id 

select * from order_items;
--Find best-selling product.
select oi.product_id,p.product_name,sum(oi.quantity) as best_sellers
from order_items oi 
JOIN products p on oi.product_id = p.product_id
group by p.product_name,oi.product_id
order by best_sellers desc 

--Total revenue per category.
select p.category,sum(p.price * oi.quantity) as total_revenue
from order_items oi 
JOIN products p on p.product_id = oi.product_id
group by p.category
order by total_revenue desc 


--Highest revenue customer.
select c.customer_name,sum(p.price * oi.quantity) as total_revenue_per_customer
from customers c
JOIN orders o on c.customer_id = o.customer_id
JOIN order_items oi on o.order_id = oi.order_id
JOIN products p on p.product_id = oi.product_id
group by c.customer_name
order by total_revenue_per_customer desc
LIMIT 1
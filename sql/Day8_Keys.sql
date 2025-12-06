select c.customer_id,c.customer_name,o.order_id,o.order_date from 
customers c 
INNER JOIN orders o
on c.customer_id = o.order_id;


--inner join 
select oi.order_id, o.customer_id, p.product_name 
from order_items oi
INNER JOIN orders o on oi.order_id = o.order_id
INNER JOIN products p on p.product_id = oi.order_id;

--left join

select c.customer_id,c.customer_name, o.order_id
from customers c 
LEFT JOIN orders o on c.customer_id = o.order_id;




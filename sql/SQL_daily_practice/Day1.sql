--Find all customers who have never placed an order.

select c.customer_name,o.order_id 
from customers c 
left join orders o on c.customer_id = o.customer_id
where o.order_id is null

--Find total number of orders per customer.
select c.customer_name,count(o.order_id) from
customers c
JOIN orders o on c.customer_id = o.customer_id
group by c.customer_name

--Find customers who placed more than 3 orders.
select * from
(select c.customer_id,count(o.order_id) as number_of_orders
from customers c 
RIGHT JOIN orders o on c.customer_id = o.customer_id
group by c.customer_id)
where number_of_orders > 3
order by number_of_orders desc 


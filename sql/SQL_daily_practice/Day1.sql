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

--Latest order from each customer

select customer_name,
order_id,
order_date
from
(select
c.customer_name,
o.order_id,
o.order_date,
ROW_NUMBER() OVER(PARTITION BY c.customer_id order by o.order_id desc
 ) as rn
from customers c 
JOIN orders o on o.customer_id = c.customer_id 
) t
where rn = 1;

--Find duplicate emails in the customers table.
select customer_name,email from
(select customer_name,email,
ROW_NUMBER() OVER(partition by email order by customer_id desc) as rn
from customers
) t 
where rn > 1



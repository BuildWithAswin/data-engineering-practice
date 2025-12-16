--Create sales_summary view.

create view sales_summary AS 
select date_trunc('day' , o.order_date)::date as sales_day, 
count (o.order_id) as total_orders,
sum(o.total_amount) as total_revenue 
from orders o 
group by sales_day 
order by sales_day asc 

select * from sales_summary;

--Create active_customers view.

CREATE VIEW active_customers AS
select c.customer_id,c.customer_name as active_customers,o.order_date
from customers c
JOIN orders o on o.customer_id = o.customer_id
where o.order_date >= '2025-12-11'
order by active_customers asc 

select * from active_customers  

--Refresh logic through base table.
insert into customers (customer_name, city,email,phone_number)
VALUES
('Allen' , 'Cochin', 'c.allen@gmail.com','1234567862')

select * from customers


ALTER TABLE customers
ALTER COLUMN customer_id
ADD GENERATED ALWAYS AS IDENTITY;

SELECT pg_get_serial_sequence('customers', 'customer_id');

SELECT last_value FROM customers_customer_id_seq;

SELECT MAX(customer_id) FROM customers;

SELECT setval(
    pg_get_serial_sequence('customers', 'customer_id'),
    (SELECT MAX(customer_id) FROM customers) + 1
);







--Raw → staging → clean table.
--Raw tables

create table raw_customers as 
select * from customers;

create table raw_orders as 
select * from orders;

--Stage layer - Technical cleanup
create table stg_customers as
select 
    customer_id,
    customer_name,
    phone_number
from raw_customers;

create table stg_orders as
select 
    order_id,
    customer_id,
    order_date,
    COALESCE(total_amount, 0) as total_amount
from raw_orders 
where order_id is not null

--clean layer

create table fact_orders as
select 
    order_id,
    customer_id,
    order_date,
    total_amount
from stg_orders;

create table fact_customers as
select 
    customer_id,
    customer_name,
    phone_number
from stg_customers;


select * from fact_orders
select * from fact_customers


drop table fact_customers;
drop table stg_customers;
drop table raw_customers

select * from customers

insert into customers (customer_name,city,email,phone_number,join_date)
values ('Suresh Jayraman', 'Kerala', 'suresh@gmail.com', 1234567898,'2020-01-01')

update  customers set join_date = '2020-01-10' where customer_id = 9;



create table stg_customers as
select 
    customer_id,
    customer_name,
    city,
    email,
    phone_number 
from (
    select *,
            row_number() OVER(
                PARTITION BY email order by join_date DESC
            ) AS rn 
    FROM raw_customers) t 
where rn = 1;

select * from stg_customers

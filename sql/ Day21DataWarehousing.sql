--Convert OLTP orders to fact table.
CREATE TABLE fact_order_items AS 
SELECT 
    o.order_id,
    oi.item_id AS order_item_id,
    o.customer_id,
    oi.product_id,
    o.order_date,
    oi.quantity,
    p.price AS unit_price,
    (oi.quantity * p.price) AS total_amount
FROM orders o
JOIN order_items oi on oi.order_id = o.order_id
JOIN products p on p.product_id = oi.product_id;

select * from fact_order_items


--Create dimension tables.

CREATE TABLE dim_customers (
    customer_key SERIAL PRIMARY KEY,
    customer_id INT,
    customer_name TEXT,
    city TEXT,
    email TEXT);

CREATE  TABLE dim_products (
    product_key SERIAL PRIMARY KEY,
    product_id INT,
    product_name TEXT,
    category TEXT,
    price NUMERIC
)

CREATE TABLE dim_date (
    date_key DATE PRIMARY KEY,
    day INT,
    month INT,
    month_name TEXT,
    year INT,
    quarter INT
);


-- LOAD DATA

INSERT INTO dim_customers (customer_id,customer_name,city,email)
SELECT customer_id,customer_name,city,email
FROM customers;

INSERT INTO dim_products (product_id,product_name,category,price)
SELECT product_id,product_name,category,price
FROM products

INSERT INTO dim_date 
SELECT DISTINCT 
    order_date,
    EXTRACT(DAY FROM order_date),
    EXTRACT(MONTH FROM order_date),
    TO_CHAR(order_date, 'Month'),
    EXTRACT (YEAR FROM order_date),
    EXTRACT(QUARTER FROM order_date)
FROM orders;

select * from fact_order_items
select * from dim_customers
select * from dim_date
select * from dim_products

--Revenue by dimension.

--Revenue by customers
select c.customer_name,
SUM(f.total_amount) as totl_amount 
from dim_customers c 
JOIN fact_order_items f on f.customer_id = c.customer_id
group by c.customer_name


--Revenue by date
select d.date_key,
sum(f.total_amount) AS total_revenue 
from dim_date d 
JOIN fact_order_items f ON f.date_key = d.date_key
group by d.date_key

--Adding date key to facts table 
alter table fact_order_items add column date_key DATE 

update fact_order_items set date_key = order_date

alter table fact_order_items
add constraint fa_fact_date
foreign key (date_key)
references dim_date(date_key)

--Revenue by products
select d.product_name,sum(f.total_amount) as revenue_per_product
from dim_products d
JOIN fact_order_items f on f.product_id = d.product_id
group by d.product_id,d.product_name
order by revenue_per_product desc 


--Monthly aggregates
--Revenue per month

select dd.month_name as month,dd.year,sum(f.total_amount) revenue 
from dim_date dd 
JOIN fact_order_items f ON dd.date_key = f.date_key 
group by dd.month_name,dd.year
order by dd.year

--Orders per month
select dd.month_name as month,dd.year,sum(f.order_id) as number_of_orders
from dim_date dd 
JOIN fact_order_items f on f.date_key = dd.date_key
group by dd.month_name,dd.year
order by dd.year 





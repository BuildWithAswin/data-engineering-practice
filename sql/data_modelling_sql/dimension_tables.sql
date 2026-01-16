--✅ Day 6 – Dimension Table Design**
--
--**Concepts**
--
--1. Dimension attributes
--2. Surrogate keys

create table dim_customers (
    customer_id INT primary key, --buisness key from oltp
    customer_name varchar(100),
    city varchar(100),
    phone_number varchar(20),
    customer_sk int -- PRIMARY KEY
)


create table dim_products (
    product_id int primary key, -- buisness key 
    product_name varchar(100),
    category varchar(100),
    price numeric(10,2),
    products_sk int primary key -- primary key 
)

create table dim_date (
    full_date date,
    day_of_month int,
    month_of_year int,
    quarter int,
    year int,
    date_sk int
)
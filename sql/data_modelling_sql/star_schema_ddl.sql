--- ☐ Write `CREATE TABLE` drafts for:
--    - `fact_orders`
--    - `dim_customers`
--    - `dim_products`


create table facts_orders as
    order_id int,
    order_item_id int,
    customer_sk int not null,
    product_sk int not null,
    order_date date not null,
    quantity int,
    unit_price int(10,2),
    total_amount int(12,2)

create table dim_customers (
    customer_sk serial primary key,
    customer_id int not null,
    customer_name text,
    city text,
    email text,
    is_current boolean  
)

create table dim_products (
    product_sk serial primary key,
    product_id int not null,
    product_name text,
    category text,
    price numeric(10,2)
)


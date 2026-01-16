create table fact_orders (
    order_id int, -- degenerate dimension
    customer_sk int not null, -- fk to dim_customers
    order_date_sk int,  -- fk to dim_date
    total_amount numeric(10,2), --measures
    is_delivered boolean,
    delivery_date_sk int --fk to dim_date

    constraint fk_customer
    foreign key (customer_sk)
    dim_customer(customer_sk)

    constraint fk_order_date
    foreign key (order_date_sk)
    dim_orders(date_sk)

    constraint fk_delivery_date
    foreign key (delivery_date_sk)
    dim_date(date_sk)
)

create table facts_order_items(
    order_id int,
    order_item_id int,
    customer_sk int, -- fk to dim_products
    product_sk int not null, -- fk to dim_products
    order_date_sk int not null, -- fk to dim_date
    quantity int --measure
    unit_price numeric(10,2), -- measure
    total_amount numeric(12,2), --measure 

    constraint fk_products
    foreign key(products_sk)
    references dim_customers(customer_sk)

    constraint fk_customers
    foreign key (customers_sk)
    references dim_customers(customers_sk)

    constraint fk_order_date
    foreign key (order_date_sk)
    references dim_date(dim_date_sk)

)


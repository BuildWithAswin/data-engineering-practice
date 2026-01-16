-- Grain: one row per order item per day

--identifiers
    order_item_id - (degenrate dimension)
    order_id - (degenerate dimension)

--Foerign keys
    customer_sk - dim_customers.customer_id
    product_sk  - dim_products.product_id
    date_sk - dim_date.date_sk
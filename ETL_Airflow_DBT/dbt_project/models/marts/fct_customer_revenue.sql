select 
    c.customer_id,
    c.email,
    sum(o.total_amount) as total_revenue
    from {{ref('stg_customers')}} c
    join {{ref('int_customer_order')}} o
        on c.customer_id = o.customer_id
    group by 1,2



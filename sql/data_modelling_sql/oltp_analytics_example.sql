--For each customer city and product category, 
--calculate the month-over-month revenue growth for the last 3 years,
-- considering only completed orders, adjusted for refunds,
-- and include customers who have changed cities during this period.
with base_sales as (
select to_char(date_trunc('month', o.order_date), 'Mon YYY') as order_month,
c.city as city,
p.category as category,
sum(oi.quantity * p.price) as net_revenue
from customers c
JOIN orders o on o.customer_id = c.customer_id
JOIN order_items oi on oi.order_id = o.order_id
JOIN products p on p.product_id = oi.product_id
where o.is_delivered = true 
and o.order_date >= CURRENT_DATE - INTERVAL '3 years'
group by to_char(date_trunc('month', order_date), 'Mon YYY'),p.category,c.city
),
mom_growth as (
    select order_month,
    city,
    category,
    net_revenue,
    LAG(net_revenue) OVER(PARTITION by city,category order by order_month) as prev_month_revenue
from base_sales
)
select 
    order_month,
    city,
    category,
    net_revenue,
    prev_month_revenue,
    CASE
        when prev_month_revenue is null then null 
        else (net_revenue - prev_month_revenue) / prev_month_revenue
    END as month_over_month_growth
    from mom_growth
    order by order_month,city,category


    





--Revenue by date

select order_date as date, 
sum(total_amount) as revenue
from fact_orders 
group by order_date
order by order_date

--Revenue by product
select dp.product_name as product,sum(oi.quantity),sum(oi.unit_price * oi.quantity) as revenue
from dim_products dp 
JOIN fact_order_items oi on oi.product_id = dp.product_id
group by dp.product_name
order by sum(oi.unit_price * oi.quantity) asc 

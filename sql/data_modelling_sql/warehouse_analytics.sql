--Revenue by date

select order_date as date, 
sum(total_amount) as revenue
from fact_orders 
group by order_date
order by order_date

--Revenue by product
select dp.product_name as product,sum(oi.quantity) as total_quantityßß,sum(oi.unit_price * oi.quantity) as revenue
from dim_products dp 
JOIN fact_order_items oi on oi.product_id = dp.product_id
group by dp.product_name
order by sum(oi.unit_price * oi.quantity) asc 

--Revenue by customer
select dc.customer_name as customer,sum(fo.total_amount) as revenue
from dim_customers dc
JOIN fact_orders fo on fo.customer_id = dc.customer_id 
group by dc.customer_name
order by sum(fo.total_amount) desc 

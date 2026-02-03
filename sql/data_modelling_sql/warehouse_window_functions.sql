--Running total revenue (Daily)
select order_date,total_amount,
sum(total_amount) over(order by order_date, order_id) as running_revenue 
from fact_orders


--Running total revenue(Monthly)
select order_id,order_date,total_amount, DATE_TRUNC('month', order_date) as month,
SUM(total_amount) OVER(PARTITION BY DATE_TRUNC('month', order_date) order by order_date, order_id ) as monthly_running_revenue
from fact_orders


--Rank customers by spend

select d.customer_id,d.customer_name, sum(total_amount) as total_spent,
RANK() OVER(order by sum(total_amount) desc) as spend_rank
from fact_orders fo
JOIN dim_customers d on d.customer_id = fo.customer_id
group by d.customer_id,d.customer_name

--MOM growth

select month,monthly_revenue, 
monthly_revenue - LAG(monthly_revenue)  OVER(order by month ) as mom_growth
from(
select DATE_TRUNC('month', order_date) as month, sum(total_amount) as monthly_revenue
from fact_orders
group by DATE_TRUNC('month', order_date)
)


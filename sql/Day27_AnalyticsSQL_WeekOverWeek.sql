--Mental model (lock this in)
    --step1.Aggregate by week
    --step2.Pull previous week’s value
    --step3.Compare current vs previous


with weekly_orders as (
    select 
    date_trunc('week', order_date) as week_start,
    count(order_id) as orders 
    from orders
    group by date_trunc('week', order_date)
),
weekly_with_prev as (
    select 
    week_start,
    orders,
    lag(orders) over(order by week_start) as previous_week_orders 
    from 
    weekly_orders
)
select  
    week_start,
    orders,
    previous_week_orders,
    ROUND(100 * (orders - previous_week_orders) / previous_week_orders,2 )
    AS wow_growth 
    from weekly_with_prev
    order by week_start


--Monthly sales using CTE.

--Normal method
select to_char(date_trunc('month' , order_date),'Mon YYYY') as month, sum(total_amount)
from orders 
group by month
order by month 

--CTE method
with monthly_sales AS (
    select to_char(date_trunc('month', order_date), 'Mon YYYY') as month, 
    sum(total_amount) as total_sales
    from orders 
    group by date_trunc('month', order_date)
    order by month 
    )
select 
    month,
    total_sales 
    from monthly_sales
order by month

--Recursive hierarchy query.

--Print number 1 to 10

with recursive numbers as    
    (select 1 as n
    union 
    select n + 1        
    from numbers where n < 10)
select * from numbers


--Rank inside CTE.
--Rank customers based on total spending inside CTE
select c.customer_name,o.total_amount,
RANK() OVER(order by o.total_amount desc) as spending_rank 
from customers c 
JOIN orders o on c.customer_id = o.customer_id
order by spending_rank desc 





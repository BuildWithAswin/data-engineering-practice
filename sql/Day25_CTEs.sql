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
with top_spending_customers AS (
select c.customer_name,sum(o.total_amount) as total_amount,
RANK() OVER(order by sum(o.total_amount) desc) as spending_rank 
from customers c 
JOIN orders o on c.customer_id = o.customer_id
group by c.customer_name
)
select 
customer_name,
total_amount,
spending_rank
from top_spending_customers

--Deduplicate using CTE.

select * from stg_customers
insert into stg_customers (customer_name,city,email,phone_number)
values 
('Allen.c', 'vypin, cochin', 'c.allen@gmail.com', '1234567874')

with dedup_stg_customers as (
select *, 
row_number() over(PARTITION by email order by customer_id desc) as rn 
from stg_customers)

select * from dedup_stg_customers
where rn =1;



--Chain multiple CTEs.
--Customers → Deduplicate → Rank
with customer_spend as(
select c.customer_id,c.customer_name,c.email,sum(o.total_amount) as total_spend
from customers c
JOIN 
orders o on c.customer_id  = o.customer_id
group by c.customer_id,c.email,c.customer_name
),
dedup_customers as
(select *,
row_number() over(PARTITION by email order by customer_id desc) as rn 
from customer_spend),
ranked_customers as (
select *,
rank() over(order by total_spend desc) as spending_rank
from dedup_customers
where rn = 1
)
select * from ranked_customers
order by spending_rank;















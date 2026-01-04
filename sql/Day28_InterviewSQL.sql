--Second highest salary.
with ranked_salary as (
    select 
    name,
    salary,
    DENSE_RANK() over(order by salary desc) as rnk 
    from employees 
) 
select name , salary 
from ranked_salary 
where rnk = 2;


--Employees without managers.
select name,manager from Employees
where manager is null 

--Gaps & islands.

select * from orders

--🔹 Step 1: Deduplicate orders to one row per customer per day
WITH daily_orders AS 
(
    select 
        customer_id,
        order_date::date AS order_date
        from orders
)

--🔹 Step 2: Order rows and look at the previous day

    , ordered_days AS (
        select 
            customer_id,
            order_date,
            LAG(order_date) OVER(PARTITION BY customer_id order by order_date)
            AS prev_order_date
        from daily_orders
    )

--🔹 Step 3: Identify where a streak breaks
    , steak_flags as (
        select 
            customer_id,
            order_date,
            CASE 
                when prev_order_date is null then 1
                when order_date - prev_order_date > 1 then 1
                else 0
            end as is_new_streak
        from ordered_days
    )


--🔹 Step 4: Assign a streak ID (this creates the “islands”)

    , streak_groups as (
        select 
            customer_id,
            order_date,
            sum(is_new_streak) over (PARTITION by customer_id
            order by order_date
            ) as streak_id  
        from streak_flags
    )
--🔹 Step 5: Aggregate each streak
    , select 
            customer_id,
            min(order_date) as streak_start_date,
            max(order_date) as streak_end_date,
            count(*) as number_of_days_in_streak
        from streak_groups
        group by customer_id,streak_id
        order by customer_id,streak_start_date



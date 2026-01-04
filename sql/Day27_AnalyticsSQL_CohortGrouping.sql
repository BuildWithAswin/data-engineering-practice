--Cohort grouping.

with cohort as (
select o.customer_id,
date_trunc('month', min(o.order_date)) as cohort_month
from orders group by customer_id
)

select cohort_month,
count(customer_id) as cohort_size 
from cohort
group by cohort_month
order by cohort_month

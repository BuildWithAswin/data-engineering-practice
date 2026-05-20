-- implement scd- type 2 columns on orders table

-- Add SCD Type 2 columns

alter table dim_customers 
add column effective_start_date date;

alter table dim_customers 
add column effective_end_date date;

alter table dim_customers 
add column is_current boolean;

-- set default for new records
alter table dim_customers 
alter column is_current set default true;

-- EXPIRE the current record (UPDATE)

update table dim_customers d
    set effective_end_date = CURRENT_DATE - INTERVAL '1 day',
    is_current = false 
from stg_customers s    
where d.customer_id = s.customer_id  
      AND d.is_current = true 
      AND (
        d.city <> s.city,
      OR d.customer_name <> s.customer_name 
      )

-- INSERT the new version (SCD Type 2)

insert int dim_customers (
    customer_sk,
    customer_id,
    customer_name,
    city,
    effective_start_date,
    effective_end_date,
    is_current
)
SELECT 
    nextval('dim_customers_customer_sk_seq'),
    s.customer_id,
    s.customer_name,
    s.city,
    CURRENT_DATE,
    NULL,
    true
FROM stg_customers s
LEFT JOIN  dim_customers d on d.customer_id = s.customer_id 
d.is_current = true
WHERE d.customer_id is NULL 
OR
(
    s.customer_name <> d.customer_name
    OR
    s.city <> d.city
)



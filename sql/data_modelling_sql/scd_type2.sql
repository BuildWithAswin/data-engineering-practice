-- implement scd- type 2 columns on orders table

alter table fact_orders 
add column effective_start_date date;

alter table dim_customers 
add column effective_end_date date;

alter table fact_orders 
add column is_current boolean;


alter table dim_customers 
alter column is_current set default true;



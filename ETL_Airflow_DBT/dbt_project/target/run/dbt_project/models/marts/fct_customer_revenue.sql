
  
    

  create  table "sql_practice"."public"."fct_customer_revenue__dbt_tmp"
  
  
    as
  
  (
    select 
    c.customer_id,
    c.email,
    sum(o.total_amount) as total_revenue
    from "sql_practice"."public"."stg_customers" c
    join "sql_practice"."public"."int_customer_order" o
        on c.customer_id = o.customer_id
    group by 1,2
  );
  
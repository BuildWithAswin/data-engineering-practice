
  create view "sql_practice"."public"."stg_customers__dbt_tmp"
    
    
  as (
    select customer_id,
        lower(email) as email,
        join_date as created_at,
        md5(email) as record_hash
from    "sql_practice"."public"."customers"
  );
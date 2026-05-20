select o.order_id,
        o.customer_id,
        o.total_amount,
        o.order_date
from "sql_practice"."public"."orders" o
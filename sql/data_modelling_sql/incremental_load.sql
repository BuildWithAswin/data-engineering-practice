--INSERT INTO fact_orders

INSERT INTO fact_orders (
    order_id,
    customer_sk,
    order_date,
    total_amount,
    is_delivered,
    delivery_date,
    customer_region
)
SELECT
    s.order_id,
    d.customer_sk,
    s.order_date,
    s.total_amount,
    s.is_delivered,
    s.delivery_date,
    d.region
FROM stg_orders s
JOIN dim_customers d
  ON s.customer_id = d.customer_id
 AND d.is_current = true
WHERE s.updated_at > (
    SELECT last_run_ts
    FROM etl_control
    WHERE job_name = 'fact_orders_load'
);

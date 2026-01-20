--add customer_region to fact_orders
ALTER table fact_orders add column customer_region varchar(50)

select * from dim_customers

update fact_orders
set customer_region = 'Asia-Pacific'

--actual prod use cases

UPDATE fact_orders f
SET customer_region = d.region
FROM dim_customers d
WHERE f.customer_sk = d.customer_sk
  AND d.is_current = true
  AND f.customer_region IS NULL;
  
--Verify before updating (best practice)  
  SELECT f.order_id, f.customer_region, d.region
FROM fact_orders f
JOIN dim_customers d
  ON f.customer_sk = d.customer_sk
WHERE f.customer_region IS NULL;
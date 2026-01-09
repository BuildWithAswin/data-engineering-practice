--Funnel analysis.

--Customers → Orders → Delivered Orders

with funnel as (
    select c.customer_id,
        CASE 
            WHEN o.order_id IS NOT NULL THEN 1 ELSE 0
        END AS placed_order, 
        CASE 
            WHEN o.is_delivered = true THEN 1 ELSE 0
        END AS delivered_order 
    from customers c 
    LEFT JOIN orders o 
        ON  o.customer_id = c.customer_id 

)
select count(*) as total_customers,
        sum(placed_order) as placed_order_customers,
        sum(delivered_order) as delivered_order_customers
from funnel;



--Funnel with conversion percentages

WITH funnel AS (
    SELECT
        c.customer_id,
        MAX(1) AS entered,
        MAX(CASE WHEN o.order_id IS NOT NULL THEN 1 ELSE 0 END) AS ordered,
        MAX(CASE WHEN o.is_delivered THEN 1 ELSE 0 END) AS delivered
    FROM customers c
    LEFT JOIN orders o
        ON o.customer_id = c.customer_id
    GROUP BY c.customer_id
)
SELECT
    'Entered funnel' AS stage,
    COUNT(*) AS users,
    round(100.0) AS pct
FROM funnel

UNION ALL

SELECT
    'Placed order',
    COUNT(*) FILTER (WHERE ordered = 1),
    round(100.0 * COUNT(*) FILTER (WHERE ordered = 1) / COUNT(*))
FROM funnel

UNION ALL

SELECT
    'Delivered order',
    COUNT(*) FILTER (WHERE delivered = 1),
    round(100.0 * COUNT(*) FILTER (WHERE delivered = 1) / COUNT(*))
FROM funnel;

--Order-Level Funnel


select 
    'created' as stage,
    count(*) as orders,
    100.0 as pct
from orders

union all

select 
    'delivered',
    count(*) filter (where is_delivered = true),
    round(100.0 * count(*) filter (where is_delivered = true) / count(*))
from orders

union all

select 
    'is_pending',
    count(*) filter (where is_delivered = false),
    round(100.0 * count(*) filter (where is_delivered = false) / count(*))
from orders


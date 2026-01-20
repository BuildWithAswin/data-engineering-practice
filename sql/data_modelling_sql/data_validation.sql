--3️⃣ Basic Row Count Reconciliation Query

SELECT COUNT(*) AS source_count
FROM orders
WHERE updated_at >= '2026-01-19 00:00:00'
  AND updated_at <  '2026-01-20 00:00:00';

--6️⃣ Group-Level Row Count Validation (Stronger Check)
Instead of one total count, compare grouped counts.

Example: Orders per day
-- Source
SELECT order_date, COUNT(*) AS cnt
FROM orders
GROUP BY order_date;

-- Target
SELECT order_date, COUNT(*) AS cnt
FROM orders_dw
GROUP BY order_date;


--3️⃣ SQL to Directly Compare Source vs Target
Example: Join-based reconciliation
SELECT
    s.order_date,
    s.cnt AS source_cnt,
    t.cnt AS target_cnt,
    (t.cnt - s.cnt) AS diff
FROM
    (SELECT order_date, COUNT(*) AS cnt
     FROM orders_source
     GROUP BY order_date) s
LEFT JOIN
    (SELECT order_date, COUNT(*) AS cnt
     FROM orders_target
     GROUP BY order_date) t
ON s.order_date = t.order_date;


================================================================================================================================================================

--Duplicate detection query

--2️⃣ Basic Duplicate Detection Query (Primary Key)
--Example: order_id should be unique
SELECT
    order_id,
    COUNT(*) AS cnt
FROM orders
GROUP BY order_id
HAVING COUNT(*) > 1;


--3️⃣ Interview Follow-up: “What if there is no single primary key?”
--Use Composite / Business Key

--Example:

--user_id + order_date

SELECT
    user_id,
    order_date,
    COUNT(*) AS cnt
FROM orders
GROUP BY user_id, order_date
HAVING COUNT(*) > 1;

--4️⃣ Duplicate Detection for Incremental Loads (Very Important)
--Scenario:

--Pipeline retries caused the same batch to load twice

--Detect duplicates within ingestion window:
SELECT
    order_id,
    COUNT(*)
FROM orders_target
WHERE ingestion_date = '2026-01-19'
GROUP BY order_id
HAVING COUNT(*) > 1;


--1️⃣ Basic duplicate detection (single column)
--Question:
--Are there duplicate order_ids?

SELECT
    order_id,
    COUNT(*) AS cnt
FROM fact_orders
GROUP BY order_id
HAVING COUNT(*) > 1;

--✔ Finds duplicate business keys
--✔ Most basic sanity check

--2️⃣ Duplicate detection at the grain (most important)
--Duplicates are defined by the grain, not by one column

--Example grain:

--One row per order item per day

select order_id,
        order_item_id,
        order_item_id 
        count(*) as cnt
from fact_orders 
group by 
    order_id,
    order_item_id,
    order_item_id
having count(*) > 1


--Full row comparison
select order_id,
        customer_id,
        order_date,
        total_amount,
        count(*) as cnt
from fact_orders
group by 
    order_id,
    customer_id,
    order_date,
    total_amount
having count(*) > 1


--5️⃣ Find duplicate rows but keep one (using window functions)
select * from 
    (select  *,
    row_number() over(PARTITION by order_id,order_item_id,order_date order by load_timestamp) as rn
from fact_orders ) t 
where rn > 1


--6️⃣ Source vs target duplicate mismatch
SELECT s.order_id
FROM stg_orders s
JOIN fact_orders f
  ON s.order_id = f.order_id
GROUP BY s.order_id
HAVING COUNT(*) > 1;

--7️⃣ Prevent duplicates proactively (best practice)
CREATE UNIQUE INDEX ux_fact_orders_grain
ON fact_orders (order_id, order_item_id, order_date);


--3️⃣ Basic measure reconciliation (source vs target)
-- Source
SELECT SUM(order_amount) AS source_total
FROM orders
WHERE order_date = DATE '2026-03-15';

-- Target
SELECT SUM(total_amount) AS target_total
FROM fact_orders
WHERE order_date = DATE '2026-03-15';

--4️⃣ Measure reconciliation for incremental loads (very common)
-- Source incremental window
SELECT SUM(order_amount) AS source_total
FROM stg_orders
WHERE updated_at > :last_run_ts
  AND updated_at <= :current_run_ts;

-- Target incremental window
SELECT SUM(total_amount) AS target_total
FROM fact_orders
WHERE load_timestamp > :last_run_ts
  AND load_timestamp <= :current_run_ts;

--5️⃣ Measure reconciliation by partition (best practice)
SELECT
    tableoid::regclass AS partition_name,
    SUM(total_amount) AS partition_total
FROM fact_orders
WHERE order_date >= DATE '2026-03-01'
  AND order_date <  DATE '2026-04-01'
GROUP BY tableoid::regclass;


--6️⃣ Measure reconciliation at the grain (advanced)          (ref notes for details)
--tableoid is a system column in PostgreSQL.Which physical table a row actually belongs to

SELECT
    tableoid::regclass AS partition_name,
    SUM(total_amount) AS partition_total
FROM fact_orders
WHERE order_date >= DATE '2026-03-01'
  AND order_date <  DATE '2026-04-01'
GROUP BY tableoid::regclass;


--7️⃣ Multi-measure reconciliation (strong interview example)
SELECT
    COUNT(*)              AS row_count,
    SUM(total_amount)     AS total_amount,
    SUM(quantity)         AS total_quantity
FROM fact_orders
WHERE order_date = DATE '2026-03-15';


--Compare this with source aggregates for the same date.

--This validates:

--Volume

--Revenue

--Units
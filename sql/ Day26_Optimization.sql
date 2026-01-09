--Identify slow query.

SELECT *
FROM orders
WHERE EXTRACT(YEAR FROM order_date) = 2023;

SELECT *
FROM orders
WHERE order_date >= '2023-01-01'
  AND order_date <  '2024-01-01';

EXPLAIN ANALYZE
SELECT *
FROM orders
WHERE customer_id = 5;



INSERT INTO orders (customer_id, order_date, total_amount, is_delivered)
SELECT
    c.customer_id,
    CURRENT_DATE - (random() * 365)::INT,
    (random() * 100000)::INT,
    random() < 0.5
FROM customers c
CROSS JOIN generate_series(1, 10000);


select count(*) from orders

SELECT COUNT(*) FROM customers;

SELECT pg_size_pretty(pg_relation_size('orders'));
SELECT pg_size_pretty(pg_total_relation_size('orders'));


--with more data

EXPLAIN ANALYZE
SELECT *
FROM orders
WHERE customer_id = 5;


Seq Scan on orders  (cost=0.00..1322.28 rows=9861 width=21) (actual time=0.012..8.474 rows=10004 loops=1)
  Filter: (customer_id = 5)
  Rows Removed by Filter: 60018
Planning Time: 0.628 ms
Execution Time: 8.836 ms

--create index
select * from orders

create index idx_orders_customer_id on orders(customer_id)



Bitmap Heap Scan on orders  (cost=112.72..682.98 rows=9861 width=21) (actual time=1.680..4.374 rows=10004 loops=1)
  Recheck Cond: (customer_id = 5)
  Heap Blocks: exact=446
  ->  Bitmap Index Scan on idx_orders_customer_id  (cost=0.00..110.25 rows=9861 width=0) (actual time=1.632..1.633 rows=10004 loops=1)
        Index Cond: (customer_id = 5)
Planning Time: 0.602 ms
Execution Time: 4.699 ms

--compare same with seq scan
SET enable_bitmapscan = off;
SET enable_indexscan = off;
SET enable_seqscan = on;


EXPLAIN ANALYZE
SELECT *
FROM orders
WHERE customer_id = 5;
SET enable_bitmapscan = off;



Bitmap Heap Scan on orders  (cost=112.72..682.98 rows=9861 width=21) (actual time=0.684..5.249 rows=10004 loops=1)
  Recheck Cond: (customer_id = 5)
  Heap Blocks: exact=446
  ->  Bitmap Index Scan on idx_orders_customer_id  (cost=0.00..110.25 rows=9861 width=0) (actual time=0.620..0.620 rows=10004 loops=1)
        Index Cond: (customer_id = 5)
Planning Time: 2.512 ms
Execution Time: 5.583 ms
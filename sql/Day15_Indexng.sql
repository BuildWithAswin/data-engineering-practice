--Add index on customer_id.
CREATE INDEX idx_customers_customer_id ON customers (customer_id);

--2. Add index on order_date.
CREATE INDEX idx_orders_order_date ON orders (order_date);

--Drop index safely.
drop index public.idx_orders_order_date

--Check query execution plan.

select * from orders
where order_date = '2025-12-12'

EXPLAIN ANALYZE
select * from orders
where order_date = '2025-12-12'

Seq Scan on orders  (cost=0.00..1.23 rows=1 width=21) (actual time=0.010..0.010 rows=1 loops=1)
  Filter: (order_date = '2025-12-12'::date)
  Rows Removed by Filter: 17
Planning Time: 0.401 ms
Execution Time: 0.019 ms

select * from orders
order by order_date desc 

EXPLAIN ANALYZE
select * from orders
where order_date = '2025-12-12'







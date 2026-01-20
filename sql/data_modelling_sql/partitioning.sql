CREATE TABLE fact_orders_new (
    order_id     INT,
    customer_id  INT,
    order_date   DATE NOT NULL,
    total_amount NUMERIC(10,2)
)
PARTITION BY RANGE (order_date);

CREATE TABLE fact_orders_2026_02
PARTITION OF fact_orders
FOR VALUES FROM ('2026-02-01') TO ('2026-03-01');

CREATE TABLE fact_orders_2026_03
PARTITION OF fact_orders
FOR VALUES FROM ('2026-03-02') TO ('2026-04-01');

CREATE TABLE fact_orders_default
PARTITION OF fact_orders
DEFAULT;

drop table fact_orders_2026_03



INSERT INTO fact_orders_new
SELECT * FROM fact_orders;





alter table fact_orders rename to fact_orders_old
alter table fact_orders_new rename to fact_orders


INSERT INTO fact_orders (
    order_id,
    customer_id,
    order_date,
    total_amount
)
VALUES
(4001, 1, DATE '2026-03-01', 1200.00),
(4002, 2, DATE '2026-03-15',  850.00),
(4003, 3, DATE '2026-03-31',  430.00),
(4004, 4, DATE '2026-04-03',  430.00),
(4005, 3, DATE '2026-04-06',  430.00),
(4006, 4, DATE '2026-04-28',  430.00);


SELECT
    order_id,
    customer_id,
    tableoid::regclass AS partition_name
FROM fact_orders
ORDER BY order_id;


EXPLAIN
SELECT SUM(total_amount)
FROM fact_orders
WHERE order_date >= '2026-03-01'
  AND order_date <  '2026-03-31';
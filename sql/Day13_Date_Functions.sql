
--Inserted new rows to orders for practicing date function
INSERT INTO orders (order_id, customer_id, order_date, total_amount, is_delivered)
VALUES 
(11, 1, CURRENT_DATE - INTERVAL '1 day', 32000, TRUE),
(12, 3, CURRENT_DATE - INTERVAL '3 days', 45000, FALSE),
(13, 2, CURRENT_DATE - INTERVAL '5 days', 18000, TRUE),
(14, 4, CURRENT_DATE - INTERVAL '7 days', 52000, TRUE),
(15, 1, CURRENT_DATE - INTERVAL '10 days', 75000, FALSE),
(16, 2, CURRENT_DATE - INTERVAL '12 days', 27000, TRUE),
(17, 5, CURRENT_DATE - INTERVAL '15 days', 69000, FALSE),
(18, 3, CURRENT_DATE - INTERVAL '20 days', 39000, TRUE),
(19, 4, CURRENT_DATE - INTERVAL '25 days', 81000, TRUE),
(20, 5, CURRENT_DATE - INTERVAL '30 days', 24000, FALSE);

INSERT INTO orders (order_id, customer_id, order_date, total_amount, is_delivered)
VALUES (21,1,CURRENT_DATE,2500,FALSE)


--Orders from this month.
select o.order_id,o.order_date 
from orders o 
where o.order_date >= DATE_TRUNC('month' , CURRENT_DATE );


--Orders from last 30 days.
select o.order_id, o.order_date
from orders o
where o.order_date >= (CURRENT_DATE - INTERVAL '30 days')
order by o.order_date asc

--Monthly sales totals.
select DATE_TRUNC('month', o.order_date) AS MONTH,SUM(o.total_amount)
from orders o
group by month
order by month asc

--Orders placed today.
select * from orders o
where o.order_date = CURRENT_DATE;

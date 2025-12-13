--Daily revenue report.
select DATE_TRUNC('day' , o.order_date)::date as day, SUM(oi.quantity * p.price) as total_revenue 
from orders o
JOIN order_items oi on oi.order_id = o.order_id
JOIN products p on p.product_id = oi.product_id
group by day 
order by day 



--adding entries to order_items for newly added
--records in orders as query was not showing detail of
--those rows
INSERT INTO order_items (item_id, order_id, product_id, quantity)
VALUES
(101, 11, 1, 2),
(102, 12, 3, 1),
(103, 13, 2, 3),
(104, 14, 5, 1),
(105, 15, 1, 2),
(106, 16, 4, 1),
(107, 17, 2, 2),
(108, 18, 3, 1),
(109, 19, 5, 3),
(110, 20, 4, 2);

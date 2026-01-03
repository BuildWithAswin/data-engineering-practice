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



--Customer purchase summary.
select c.customer_id,c.customer_name,SUM(o.total_amount) as total_spend,COUNT(o.order_id) as total_orders
from customers c 
 JOIN orders o on c.customer_id = o.customer_id
group by c.customer_id ,c.customer_name
order by total_spend desc 

--Product-wise sales report.
select p.product_id, p.product_name, sum(oi.quantity * p.price) as revenue
from Products p 
join order_items oi on oi.product_id = p.product_id
group by p.product_id,p.product_name
order by revenue desc 

--Peak sales day.
select o.order_date as peak_sales_day,
        count(o.order_id) as total_orders, 
        sum(o.total_amount) total_revenue
from orders o
group by o.order_date
order by total_revenue desc 
LIMIT 1

--Revenue trend by month.
select to_char(date_trunc('month' , o.order_date), 'MM-YYYY') as sales_month,
        count(o.order_id) as total_orders, 
        sum(o.total_amount) total_revenue,
    CASE
        WHEN sum(o.total_amount) >= 50000 THEN 'HIGH'
        WHEN sum(o.total_amount) >= 20000 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS category
    from orders o
    group by sales_month
    order by total_revenue desc 



from orders o
group by o.order_date
order by total_revenue desc 

SELECT DATE_TRUNC('month', order_date);

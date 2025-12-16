
--Procedure to fetch customer orders.

DROP FUNCTION IF EXISTS get_order_details(INT);

CREATE OR REPLACE FUNCTION get_order_details(
    p_customer_id INT
)
RETURNS TABLE (
    customer_id INT,
    customer_name TEXT,
    order_date DATE,
    product_name TEXT,
    quantity INT,
    price INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        c.customer_id,
        c.customer_name,
        o.order_date,
        p.product_name,
        oi.quantity,
        p.price
    FROM customers c 
    JOIN orders o ON o.customer_id = c.customer_id 
    JOIN order_items oi ON oi.order_id = o.order_id
    JOIN products p ON p.product_id = oi.product_id
    WHERE o.customer_id = 2
    ORDER BY p.price DESC;
END;
$$;


SELECT * FROM get_order_details(5);


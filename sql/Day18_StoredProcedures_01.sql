--Procedure to insert order.

--creating custom datatype to include values. Because one sigle order might 
--have different products and quantity
CREATE TYPE order_item_input AS (
    product_id INT,
    quantity INT
);

--p item is  nested array with product id and quantity (order_item_input)
CREATE OR REPLACE FUNCTION create_order(
    p_customer_id INT,
    p_items order_item_input[] 
)
RETURNS INT
LANGUAGE plpgsql
AS $$               
DECLARE
    v_order_id INT;
BEGIN
    -- Step 1: Insert into orders (temporary total = 0)
    INSERT INTO orders (customer_id, order_date, total_amount, is_delivered)
    VALUES (p_customer_id, CURRENT_DATE, 0, FALSE)
    RETURNING order_id INTO v_order_id;

    -- Step 2: Insert each order item
    INSERT INTO order_items (order_id, product_id, quantity)
    SELECT v_order_id, (item).product_id, (item).quantity
    FROM unnest(p_items) AS item; --opening the array 

    -- Step 3: Calculate total amount from products × quantity
    UPDATE orders o
    SET total_amount = (
        SELECT SUM(oi.quantity * p.price)
        FROM order_items oi
        JOIN products p ON p.product_id = oi.product_id
        WHERE oi.order_id = v_order_id
    )
    WHERE o.order_id = v_order_id;

    -- Return the new order_id
    RETURN v_order_id;
END;
$$;


--Calling the function 
--ROW(1,2).. -interpret this ROW as an order_item_input type.ROW() is a row constructor.
SELECT create_order(
    5,
    ARRAY[
        ROW(1, 2)::order_item_input, 
        ROW(3, 1)::order_item_input
    ]
);

-----------------------------------------           

SELECT setval(
    pg_get_serial_sequence('order_items', 'item_id'),
    (SELECT MAX(customer_id) FROM customers) + 1
);

ALTER TABLE order_items
ALTER COLUMN item_id
ADD GENERATED ALWAYS AS IDENTITY;


SELECT setval(
    pg_get_serial_sequence('order_items', 'item_id'),
    (SELECT COALESCE(MAX(item_id), 0) FROM order_items) + 1,
    false
);





--Use commit correctly.
drop function create_order(INT, order_item_input[] )
drop type order_item_input

CREATE TYPE order_item_input as (
    product_id INT,
    quantity INT
)
CREATE OR REPLACE FUNCTION create_order (
        p_customer_id INT,
        p_items order_item_input []
    )
    RETURNS INT
    LANGUAGE plpgsql
    AS $$
    DECLARE 
        v_order_id INT;
    BEGIN
    INSERT INTO orders (customer_id,order_date,total_amount,is_delivered,delivery_date)
    values (p_customer_id,CURRENT_DATE,0,false,null)
    RETURNING order_id INTO v_order_id;


    INSERT INTO order_items(order_id,product_id,quantity) 
    select v_order_id, (items).product_id, (items).quantity
    from unnest(p_items) as items;

    update orders o
    set total_amount =
        (select  sum (oi.quantity * p.price)
        from order_items oi
        JOIN products p on p.product_id = oi.product_id 
        where o.order_id = v_order_id
        )
    where o.order_id = v_order_id;

    RETURN v_order_id;
END;
$$;


select count(*)from orders
select count(*) from products

select create_order(
4, 
ARRAY [
    ROW(1,1)::order_item_input,
    ROW(3,5)::order_item_input
])

COMMIT;






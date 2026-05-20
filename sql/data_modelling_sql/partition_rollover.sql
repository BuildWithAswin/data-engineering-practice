CREATE OR REPLACE PROCEDURE create_fact_orders_partitions(
    months_ahead INT DEFAULT 2
)
LANGUAGE plpgsql
AS $$
DECLARE
    start_date DATE := date_trunc('month', CURRENT_DATE);
    end_date   DATE := start_date + (months_ahead || ' months')::INTERVAL;
    part_start DATE;
    part_end   DATE;
    part_name  TEXT;
BEGIN
    part_start := start_date;

    WHILE part_start < end_date LOOP
        part_end := part_start + INTERVAL '1 month';
        part_name := 'fact_orders_' || to_char(part_start, 'YYYY_MM');

        EXECUTE format(
            'CREATE TABLE IF NOT EXISTS %I PARTITION OF fact_orders
             FOR VALUES FROM (%L) TO (%L)',
            part_name, part_start, part_end
        );

        part_start := part_end;
    END LOOP;
END;
$$;

CALL create_fact_orders_partitions();


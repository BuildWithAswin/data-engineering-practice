--Procedure to update salary multiple employees
CREATE TYPE salary_update_input AS (
    empl_id INT,
    new_salary INT
)
CREATE OR REPLACE FUNCTION update_multiple_salaries(
    p_updates salary_update_input[]
)
RETURNS TABLE (
    empl_id INT,
    empl_name TEXT,
    old_salary INT,
    new_salary INT
)
LANGUAGE plpgsql
AS $$
DECLARE 
     rec salary_update_input;
     v_old_salary INT;
     v_name TEXT;
BEGIN
    FOR EACH rec in ARRAY p_updates
    LOOP
--capture old salary info
     select name,salary INTO v_name,v_old_salary 
     from employees 
     where id = rec.empl_id;
--update salary
     update employees 
     set salary = rec.new_salary
     where id = rec.empl_id;
--return row
    empl_id := rec.empl_id;
    empl_name := v_name;
    old_salary := v_old_salary;
    new_salary := rec.new_salary;

    RETURN NEXT;
 END LOOP;
END;
$$

select * from employees
order by id asc;


--CALLING FUNCTION
select * from update_multiple_salaries(
    ARRAY[
        ROW (7, 80000)::salary_update_input,
        ROW (8,63000)::salary_update_input,
        ROW (9, 71000)::salary_update_input
    ]
);

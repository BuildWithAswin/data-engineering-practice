--Procedure to update salary.

DROP FUNCTION IF EXISTS update_salary(a INT, b INT);

CREATE OR REPLACE FUNCTION update_salary(
    p_employee_id INT,
    p_salary INT
)
RETURNS TABLE(
    empl_id INT,
    employee_name TEXT,
    new_salary INT
)
LANGUAGE plpgsql
AS $$
BEGIN 
    RETURN QUERY 
    UPDATE employees
    SET salary = p_salary
    WHERE id = p_employee_id 
    RETURNING id, name::TEXT,salary;
END;
$$


select * from employees;

select * from update_salary(1, 70000)


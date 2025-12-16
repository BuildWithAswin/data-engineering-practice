--Procedure to update salary and show old and new salary

CREATE OR REPLACE FUNCTION update_salary_v2(
    p_empl_id INT,
    p_new_salary INT
)
RETURNS TABLE(
    empl_id INT,
    empl_name TEXT,
    old_salary INT,
    new_salary INT
)
LANGUAGE plpgsql
AS $$
DECLARE 
    v_old_salary INT;
    v_name TEXT;
BEGIN 
--step1 , capture old salary and name 
    select salary, name INTO v_old_salary, v_name
    FROM employees
    WHERE id = p_empl_id;

--step2, update employee salary 
    update employees
    set salary = p_new_salary
    where id = p_empl_id;

--step3, return old and new values
    empl_id := p_empl_id;
    empl_name := v_name;
    old_salary := v_old_salary;
    new_salary := p_new_salary;

RETURN NEXT;
END;
$$  

select * from employees
select * from update_salary_v2(2, 47000)



--Classify salary as High / Medium / Low.
select e.name,e.salary
CASE 
    WHEN e.salary <=  20000 THEN 'LOW'
    WHEN e.salary BETWEEN 20000 AND 50000 THEN 'MEDIUM'
    WHEN e.salary >= 50000 THEN 'HIGH'
END AS salary_category
from employees e 

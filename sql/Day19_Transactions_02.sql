--Simulate failure with rollback.

select * from accounts
--Method 1 — Simulate failure inside using SQL block

BEGIN;
DO $$ 
BEGIN
update accounts 
set balance = balance + 8000
where account_id = 3;

RAISE EXCEPTION 'Simulated failure! - something went wrong';
END
$$;


COMMIT; 


--Method 2 — Simulate failure inside PL/pgSQL block
BEGIN;
DO $$
DECLARE
    simulate_failure BOOLEAN := TRUE;
BEGIN

update accounts 
set balance = balance - 8000
where account_id = 3;

if simulate_failure THEN
RAISE EXCEPTION 'Simulated failure! - something went wrong';
END If;


update accounts
set balance = balance + 8000
where account_id = 2;

END;
$$;

COMMIT;



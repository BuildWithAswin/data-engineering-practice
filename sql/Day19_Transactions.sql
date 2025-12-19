--Transfer money between two accounts.
--1. check acc A has   sufficient balanace 
    --if acc A has balance , 
 --2. update acc B with new balance
 --3. reduce bala from A
 --4. display msg showing status 

BEGIN;

-- Anonymous block for validation logic
DO $$
DECLARE
    sender_balance NUMERIC;
    transfer_amount NUMERIC := 60000;
    sender_id INT := 1;
    reciever_id INT := 2;

BEGIN
-- 1. Fetch sender balance
select balance INTO sender_balance 
from accounts 
where account_id = sender_id;
-- 2. Check sufficient funds
IF sender_balance < transfer_amount THEN
    RAISE EXCEPTION 'TRANSFER FAILED ,INSUFFICIENT BALANCE (%)' , sender_balance;
END IF;
END
$$;
-- 3. Deduct from sender
update accounts
set balance = balance - 60000
where account_id = 2;

-- 4. Add to receiver
update accounts
set balance = balance + 60000
where account_id = 2;

COMMIT;


select * from accounts
order by account_id


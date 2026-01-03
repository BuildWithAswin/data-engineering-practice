BEGIN;

UPDATE accounts
SET balance = balance + 8000
WHERE account_id = 3;

UPDATE accounts
SET balance = balance - 8000
WHERE account_id = 2;

INSERT INTO transactions_log (account_id, amount, status, created_at)
VALUES (3, +8000, 'Transfer out', CURRENT_DATE);

DO $$
BEGIN 
    RAISE EXCEPTION 'Simulated failure!';
END
$$;

COMMIT;

select * from transactions_log

select * from accounts;




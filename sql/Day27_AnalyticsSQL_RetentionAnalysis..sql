--Retension analysis

--Retention analysis (SQL, step-by-step)
--What is retention analysis?

--Retention analysis measures how many users return and stay active over time after their first activity.

--Typical questions it answers:

--Of customers who ordered in Month 0, how many ordered again in Month 1, Month 2, …?

--Where do users drop off?

--Key idea: cohort + time since first activity.

--Your schema (assumed)

--customers(customer_id, …)

--orders(order_id, customer_id, order_date, …)

--We’ll do monthly retention based on orders.

--Step 1️⃣ Define the cohort (first order month)

--For each customer, find when they first ordered.

WITH first_order AS (
    SELECT
        customer_id,
        date_trunc('month', MIN(order_date)) AS cohort_month
    FROM orders
    GROUP BY customer_id
)

--This creates one row per customer with their cohort month.
--
--Example result:
--
--customer_id	cohort_month
--1	            2024-01-01
--2	            2024-02-01

--Step 2️⃣ Map every order to “months since first order”    
, activity AS (
    SELECT
        o.customer_id,
        f.cohort_month,
        date_trunc('month', o.order_date) AS order_month,
        (
          EXTRACT(YEAR FROM age(date_trunc('month', o.order_date), f.cohort_month)) * 12
          + EXTRACT(MONTH FROM age(date_trunc('month', o.order_date), f.cohort_month))
        ) AS month_number
    FROM orders o
    JOIN first_order f
      ON f.customer_id = o.customer_id
)

--Now each order has:
--
--month_number = 0 → first month
--
--1 → next month
--
--2 → two months later, etc.

--Step 3️⃣ Deduplicate (one customer per cohort per month)
, cohort_activity AS (
    SELECT DISTINCT
        cohort_month,
        customer_id,
        month_number
    FROM activity
),

--This ensures:
--A customer is counted once per month

--Step 4️⃣ Count retained users per cohort per month



--Step 5️⃣ Convert counts to retention percentages

cohort_size AS (
    SELECT
        cohort_month,
        COUNT(*) AS cohort_users
    FROM cohort_activity
    WHERE month_number = 0
    GROUP BY cohort_month
)
SELECT
    c.cohort_month,
    c.month_number,
    COUNT(c.customer_id) AS retained_users,
    ROUND(
        100.0 * COUNT(c.customer_id) / s.cohort_users,
        2
    ) AS retention_pct
FROM cohort_activity c
JOIN cohort_size s
  ON s.cohort_month = c.cohort_month
GROUP BY
    c.cohort_month,
    c.month_number,
    s.cohort_users
ORDER BY
    c.cohort_month,
    c.month_number;
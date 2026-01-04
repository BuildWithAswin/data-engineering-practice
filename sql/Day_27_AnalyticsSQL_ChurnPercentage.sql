

WITH first_order AS (
    SELECT
        customer_id,
        date_trunc('month', MIN(order_date)) AS cohort_month
    FROM orders
    GROUP BY customer_id
), 
activity AS (
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
), 
cohort_activity AS (
    SELECT DISTINCT
        cohort_month,
        customer_id,
        month_number
    FROM activity
),
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
        100.0 * s.cohort_users - COUNT(c.customer_id) / s.cohort_users,
        2
    ) AS churn_pct
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
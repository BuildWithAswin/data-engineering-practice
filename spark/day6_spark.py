from db import read_data
from pyspark.sql.functions import sum, avg, count

df = read_data("""
(
    select order_date, sum(total_amount) as daily_sales,
    CAST(ROUND(AVG(total_amount)::numeric,2)AS DECIMAL(10,2)) as avg_order_value
    from orders 
    group by order_date
    order by daily_sales desc
) as temp
""").show()

select customer_id,
        lower(email) as email,
        join_date as created_at,
        md5(email) as record_hash
from    {{source('raw','customers')}}




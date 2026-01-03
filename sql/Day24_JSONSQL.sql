--Extract name from JSON column.

create table raw_user_profiles (
    user_id INT,
    profile JSONB
)

insert into raw_user_profiles values 
(1,'{"name":"Aswin", "email":"aswin@gmail.com"}'),
(2,'{"name":"Rahul", "email":"rahul@gmail.com"}');

select * from raw_user_profiles

create table stg_user_profiles AS
select 
    user_id,
    profile ->> 'name' AS name 
FROM raw_user_profiles;

select * from stg_user_profiles

--Extract nested JSON value.
SELECT
    user_id,
    profile ->'adress' ->> 'city' AS city
FROM raw_user_profiles

--Filter records based on JSON field.
CREATE TABLE raw_events (
    event_id  SERIAL PRIMARY KEY,
    payload JSONB
);

drop table raw_events

insert into raw_events (payload)
values
('{"status": "active",
  "payment": { "method": "UPI" },
  "severity": 4}')

  SELECT * from raw_events
  where payload ->> 'status' = 'active'

  --Update JSON values.
  update raw_user_profiles
  set profile = jsonb_set(profile,'{name}','"Aswin kumar"')

  --Convert JSON to relational form.
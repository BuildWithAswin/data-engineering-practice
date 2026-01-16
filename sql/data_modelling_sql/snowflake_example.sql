--Normalize one dimension (e.g., product → category table)

create table dim_category (
    caetgory_sk serial primary key,
    category_name varchar(100) not null
)

create table dim_products(
    product_sk serial primary key,
    product_id INT, --business key
    product_name varchar(100),
    category_sk INT not null 

    constraint fk_category
        foreign_key  (category_sk)
        references dim_category(category_sk)

)
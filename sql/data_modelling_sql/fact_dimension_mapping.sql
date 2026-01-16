/*
========================================
DATA MODEL OVERVIEW (STAR SCHEMA)
========================================

FACT TABLE
----------
fact_sales

Grain:
- One row per product per order (line item)

FOREIGN KEYS (References to Dimension Surrogate Keys)
----------------------------------------------------
- customer_sk   → dim_customer.customer_sk
- product_sk    → dim_product.product_sk
- date_sk       → dim_date.date_sk
- order_status_sk → dim_order_status.order_status_sk

MEASURES (Numeric, Aggregatable)
--------------------------------
- sales_amount        → SUM
- quantity            → SUM
- discount_amount     → SUM
- net_revenue         → SUM (derived)
- order_count         → COUNT

========================================

DIMENSION TABLES
----------------

dim_customer
------------
- customer_sk (PK, surrogate key)
- customer_id (business / natural key)
- customer_name
- city
- state
- country
- segment
- start_date
- end_date
- is_current

dim_product
-----------
- product_sk (PK, surrogate key)
- product_id (business key)
- product_name
- category
- brand

dim_date
--------
- date_sk (PK, surrogate key)
- full_date
- day
- month
- quarter
- year

dim_order_status
----------------
- order_status_sk (PK, surrogate key)
- order_status

========================================

IMPORTANT NOTES
---------------
- Surrogate keys (_sk) are GENERATED in dimension tables
- Fact tables STORE foreign keys referencing those surrogate keys
- Fact tables never store natural/business keys
- Facts never change; dimensions manage history (SCD Type 2)
- Queries always follow: fact → dimension joins

========================================
*/

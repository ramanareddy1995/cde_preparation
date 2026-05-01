CREATE OR REPLACE TABLE stg_customers (
    customer_id INT,
    name STRING,
    city STRING
);

CREATE OR REPLACE TABLE dim_customers (
    customer_id INT,
    name STRING,
    city STRING,
    start_date DATE,
    end_date DATE,
    is_current BOOLEAN
);
INSERT INTO dim_customers VALUES
(1, 'John', 'NY', '2024-01-01', NULL, TRUE),
(2, 'Alice', 'LA', '2024-01-01', NULL, TRUE);

INSERT INTO stg_customers VALUES
(1, 'John', 'Chicago'),  -- changed city
(2, 'Alice', 'LA'),      -- no change
(3, 'Bob', 'Texas');     -- new record

 --expires old records and update the new data from existing data
UPDATE dim_customers d 
set end_date = current_date, 
    is_current = FALSE
from stg_customers s
where d.customer_id = s.customer_id
and d.is_current=TRUE
and(d.city<>s.city or
    d.name<>s.name
    );

--insert new rows  into target table
insert into dim_customers (customer_id,name,city,start_date,end_date,is_current)
select s.customer_id,
       s.name,
       s.city,
       current_date,
       null,
       True
from stg_customers s 
left join dim_customers d 
 on s.customer_id = d.customer_id
 and d.is_current = TRUE
where d.customer_id is null
or(d.name <> s.name or 
   d.city <> s.city);

   select *  from dim_customers



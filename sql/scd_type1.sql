-- Setting up Source Data
CREATE OR REPLACE TABLE STG_EMPLOYEES(
    EMPLOYEE_ID    NUMBER(6,0),
    EMPLOYEE_NAME  VARCHAR(256),
    SALARY         NUMBER(8,2),
    DEPARTMENT_ID  NUMBER(4,0)
);

INSERT INTO STG_EMPLOYEES (EMPLOYEE_ID, EMPLOYEE_NAME, SALARY, DEPARTMENT_ID) VALUES
    (101, 'Tony Stark',       150000.00, 10),   -- Engineering
    (102, 'Bruce Banner',      98000.00, 20),   -- Research
    (103, 'Peter Parker',      65000.00, 30),   -- Photography
    (104, 'Natasha Romanoff', 120000.00, 40);   -- Security
;

SELECT * FROM STG_EMPLOYEES;

-- Creating SCD Type-1 Dimension table
CREATE OR REPLACE TABLE DIM_EMPLOYEES(
    EMPLOYEE_ID    NUMBER(6,0),
    EMPLOYEE_NAME  VARCHAR(256),
    SALARY         NUMBER(8,2),
    DEPARTMENT_ID  NUMBER(4,0),
    CHECKSUM       VARCHAR(256),
    CREATED_TIMESTAMP TIMESTAMP_NTZ,
    UPDATED_TIMESTAMP TIMESTAMP_NTZ
);
-- Generating Cheksum for change detection
SELECT
    EMPLOYEE_ID,  
    UPPER(TRIM(EMPLOYEE_NAME)) AS EMPLOYEE_NAME,
    SALARY,
    DEPARTMENT_ID,
    MD5(CONCAT(
        EMPLOYEE_ID::STRING, '|',
        UPPER(TRIM(EMPLOYEE_NAME)), '|',
        SALARY::STRING, '|',
        DEPARTMENT_ID::STRING
    )) AS CHECKSUM
FROM STG_EMPLOYEES;

-- Merge Logic for SCD Type-1 
MERGE INTO DIM_EMPLOYEES tgt
USING (
    SELECT
        EMPLOYEE_ID,  
        UPPER(TRIM(EMPLOYEE_NAME)) AS EMPLOYEE_NAME,
        SALARY,
        DEPARTMENT_ID,
        MD5(CONCAT(
            EMPLOYEE_ID::STRING, '|',
            UPPER(TRIM(EMPLOYEE_NAME)), '|',
            SALARY::STRING, '|',
            DEPARTMENT_ID::STRING
        )) AS CHECKSUM
    FROM STG_EMPLOYEES
) src
ON tgt.EMPLOYEE_ID = src.EMPLOYEE_ID

-- Update record if already existing and change is detected
WHEN MATCHED AND tgt.CHECKSUM != src.CHECKSUM THEN
    UPDATE SET
        tgt.EMPLOYEE_NAME     = src.EMPLOYEE_NAME,
        tgt.SALARY            = src.SALARY,
        tgt.DEPARTMENT_ID     = src.DEPARTMENT_ID,
        tgt.CHECKSUM          = src.CHECKSUM,
        tgt.UPDATED_TIMESTAMP = CURRENT_TIMESTAMP()

-- Insert record if no match found
WHEN NOT MATCHED THEN
    INSERT (EMPLOYEE_ID, EMPLOYEE_NAME, SALARY, DEPARTMENT_ID, CHECKSUM, CREATED_TIMESTAMP, UPDATED_TIMESTAMP)
    VALUES (src.EMPLOYEE_ID, src.EMPLOYEE_NAME, src.SALARY, src.DEPARTMENT_ID, src.CHECKSUM, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP())
;

-- Updated source data to demonstarte SCD Type-1 behaviour
TRUNCATE TABLE STG_EMPLOYEES;

INSERT INTO STG_EMPLOYEES (EMPLOYEE_ID, EMPLOYEE_NAME, SALARY, DEPARTMENT_ID) VALUES
    (101, 'Tony Stark',       150000.00, 10),   -- No change
    (102, 'Bruce Banner',     100000.00, 20),   -- Salary updated
    (103, 'Peter Parker',      65000.00, 30),   -- No change
    (104, 'Natasha Romanoff', 125000.00, 40),   -- Salary updated
    (105, 'Steve Rogers',     110000.00, 50),   -- New employee
    (106, 'Thor Odinson',     130000.00, 60);   -- New employee

;

select * from dim_employees
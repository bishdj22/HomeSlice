DROP TABLE zillow1;

SELECT * FROM sales_price;

select 'zip_code',data_type 
from information_schema.columns 
where table_name = 'sales_price';

SELECT zip_code FROM sales_price 
WHERE CAST(zip_code AS VARCHAR(10)) LIKE '100%';
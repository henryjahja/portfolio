CREATE TABLE transactions (
  transaction_id SERIAL PRIMARY KEY,
  customer_id INTEGER,
  product_id INTEGER,
  transaction_date DATE,
  quantity INTEGER,
  unit_price FLOAT8,
  discount FLOAT8,
  pre_discount_total_price DOUBLE PRECISION,
  grand_total_price DOUBLE PRECISION,
  payment_method VARCHAR(50),
  employee_id INTEGER,
  credit_card_number VARCHAR(50),
  credit_card_type VARCHAR(50)
);

COPY transactions (transaction_id,customer_id,product_id,transaction_date,quantity,unit_price,discount,pre_discount_total_price,grand_total_price,payment_method,employee_id,credit_card_number,credit_card_type)
FROM 'C:\GitHub\Portfolio\Data\SQL\Transaction Data.csv'
DELIMITER ','
CSV HEADER;
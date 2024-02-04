CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  email VARCHAR(255),
  phone_number VARCHAR(255),
  address VARCHAR(255),
  city VARCHAR(255),
  state VARCHAR(255),
  postal_code VARCHAR(255),
  country VARCHAR(255),
  date_of_birth VARCHAR(255),
  gender VARCHAR(255),
  nationality VARCHAR(255),
  job_title VARCHAR(255),
  department VARCHAR(255),
  salary VARCHAR(255),
  hire_date VARCHAR(255),
  termination_date VARCHAR(255),
  manager_id INTEGER,
  employee_status VARCHAR(255),
  performance_rating VARCHAR(255),
  work_location VARCHAR(255),
  employee_type VARCHAR(255),
  employee_id INTEGER,
  supervisor_id INTEGER
);

COPY users (user_id,first_name,last_name,email,phone_number,address,city,state,postal_code,country,date_of_birth,gender,nationality,job_title,department,salary,hire_date,termination_date,manager_id,employee_status,performance_rating,work_location,employee_type,employee_id,supervisor_id)
FROM 'C:\GitHub\Portfolio\Data\SQL\User Data.csv'
DELIMITER ','
CSV HEADER;


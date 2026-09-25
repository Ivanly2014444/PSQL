CREATE TABLE employee(
    employee_id serial PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    title VARCHAR(100),
    birth_date DATE,
    notes TEXT
);

CREATE TABLE customers(
    customer_id VARCHAR(10) PRIMARY KEY,
    company_name VARCHAR(100) not NULL,
	contact_name VARCHAR(100) not NULL
);

CREATE TABLE orders(
    order_id int PRIMARY KEY,
    customer_id VARCHAR(10) REFERENCES customers(customer_id) NOT NULL,
    employee_id int REFERENCES employee(employee_id) NOT NULL,
    order_date DATE NOT NULL,
    ship_city VARCHAR(100) NOT NULL
);
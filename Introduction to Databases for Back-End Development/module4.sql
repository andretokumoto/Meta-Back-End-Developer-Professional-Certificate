CREATE DATABASE shopping_cad_db;

USE shopping_cad_db;

CREATE Table custumer(

    custumer_id INT,
    name VARCHAR(100),
    email VARCHAR(100),
    PRIMARY KEY (custumer_id)
);

CREATE TABLE product(

    product_id INT,
    name VARCHAR(50),
    PRIMARY KEY (product_id)
);

CREATE TABLE card_order(

    order_id INT,
    custumer_id INT,
    product_id INT,
    order_date DATE,
    status VARCHAR(100),
    PRIMARY KEY (order_id),
    FOREIGN KEY(custumer_id) REFERENCES custumer(custumer_id),
    FOREIGN KEY(product_id) REFERENCES product(product_id)

);

CREATE TABLE tbl( 

    table_id INT, 
    location VARCHAR(255), 
    PRIMARY KEY (table_id) 
); 

CREATE TABLE reservation( 

    reservation_id INT, 
    date_time DATETIME, 
    no_of_pax INT, 
    order_id INT, 
    table_id INT, 
    custumer_id INT, 
    PRIMARY KEY (reservation_id), 
    FOREIGN KEY (order_id) REFERENCES card_order(order_id), 
    FOREIGN KEY (table_id) REFERENCES tbl(table_id), 
    FOREIGN KEY (custumer_id) REFERENCES custumer(custumer_id) 
); 
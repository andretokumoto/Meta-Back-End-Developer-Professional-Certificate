-- Active: 1734701809361@@127.0.0.1@3306@littlelemon
USE littlelemon;

CREATE TABLE Booking(
    booking_id INT,
    name VARCHAR(255),
    NO_of_guests INT(6),
    bookingDate DATETIME,
    PRIMARY KEY(booking_id)
);
CREATE TABLE Menu(
    menu_id INT(5),
    Title VARCHAR(255),
    Price DECIMAL(10,2),
    Inventory INT(5),
    PRIMARY KEY (menu_id)
);



CREATE DATABASE ClubHopper
GO

USE ClubHopper;

CREATE TABLE users (
    email VARCHAR(50) NOT NULL PRIMARY KEY,
    password VARCHAR(64) NOT NULL
);


CREATE TABLE user_details (
	userID int IDENTITY(30000,1),
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address_line_1 VARCHAR(100) NOT NULL,
  address_line_2 VARCHAR(100),
  city VARCHAR(50) NOT NULL,
  province VARCHAR(50) NOT NULL,
  postal_code VARCHAR(20) NOT NULL,
  country VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL PRIMARY KEY,
  password VARCHAR(64) NOT NULL,
  registraion_date DATETIME DEFAULT GETDATE()
);


INSERT INTO user_details (first_name, last_name, phone_number, address_line_1, address_line_2, city, province, postal_code, country, email, password)
VALUES
('John', 'Smith', '2225557777', '222 Main St', 'Suite 100', 'Sometown', 'Manitoba', 'R1A1A1', 'Canada', 'user', '04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb'),
('John', 'Doe', '1234567890', '123 Main St', NULL, 'Anytown', 'Ontario', 'A1B2C3', 'Canada', 'john.doe@example.com', '04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb'),
('Jane', 'Smith', '0987654321', '456 Elm St', 'Apt 10', 'Othertown', 'Quebec', 'D4E5F6', 'Canada', 'jane.smith@example.com', '04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb'),
('Mike', 'Johnson', '5551234567', '789 Oak St', 'Suite 200', 'Bigcity', 'California', '12345', 'USA', 'mike.johnson@example.com', '04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb'),
('Sarah', 'Lee', '6667778888', '321 Birch Rd', NULL, 'Smalltown', 'Alberta', 'X1Y2Z3', 'Canada', 'sarah.lee@example.com', '04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb'),
('Bob', 'Jones', '3334445555', '111 Pine Ave', NULL, 'Anothercity', 'Florida', '54321', 'USA', 'bob.jones@example.com', 'password'),
('Karen', 'Nguyen', '2223334444', '555 Cedar St', 'Unit 5', 'Nexttown', 'Ontario', 'M1N2O3', 'Canada', 'karen.nguyen@example.com', '04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb'),
('Peter', 'Kim', '7778889999', '777 Cherry St', 'Apt 15B', 'Metropolis', 'New York', '10001', 'USA', 'peter.kim@example.com', '04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb'),
('Linda', 'Chen', '1112223333', '888 Maple Rd', NULL, 'Hometown', 'British Columbia', 'V1W2X3', 'Canada', 'linda.chen@example.com', '04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb'),
('David', 'Wang', '4445556666', '999 Oakwood Blvd', 'Suite 500', 'Megacity', 'Illinois', '67890', 'USA', 'david.wang@example.com', '04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb'),
('Grace', 'Chung', '9998887777', '333 Pine St', NULL, 'Smallville', 'Saskatchewan', 'S7K2C2', 'Canada', 'grace.chung@example.com', '04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb'),
('user', 'Smith', '2225557777', '222 Main St', 'Suite 100', 'Sometown', 'Manitoba', 'R1A1A1', 'Canada', 'tom.smith@example.com', '04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb');


CREATE TABLE user_approval (
  email VARCHAR(100) NOT NULL foreign key References user_details(email),
  approval_status VARCHAR(1) DEFAULT 'Y'
);


Create Table ClubOwnerDetails
(
OwnerEmail varchar(50) primary key,
ClubOwnerName varchar(50) NOT NULL,
ClubName varchar(80) NOT NULL,
OwnerPhone varchar(20) NOT NULL,
password VARCHAR(64) NOT NULL,
);


INSERT INTO ClubOwnerDetails (OwnerEmail, ClubOwnerName, ClubName, OwnerPhone, password)
VALUES
('owner1@clubhopper.com', 'John Smith', 'The Clubhouse', '555-1234', '4c1029697ee358715d3a14a2add817c4b01651440de808371f78165ac90dc581'),
('owner2@clubhopper.com', 'Jane Doe', 'The Lounge', '555-5678', '4c1029697ee358715d3a14a2add817c4b01651440de808371f78165ac90dc581'),
('owner3@clubhopper.com', 'Bob Johnson', 'The Spot', '555-9012', '4c1029697ee358715d3a14a2add817c4b01651440de808371f78165ac90dc581'),
('owner4@clubhopper.com', 'Amy Lee', 'The Cave', '555-3456', '4c1029697ee358715d3a14a2add817c4b01651440de808371f78165ac90dc581'),
('owner5@clubhopper.com', 'David Kim', 'The Hive', '555-7890', '4c1029697ee358715d3a14a2add817c4b01651440de808371f78165ac90dc581'),
('owner6@clubhopper.com', 'Jason Lee', 'The Jazz Club', '555-7890', '4c1029697ee358715d3a14a2add817c4b01651440de808371f78165ac90dc581'),
('owner7@clubhopper.com', 'Anna Kim', 'The Rooftop', '555-2345', '4c1029697ee358715d3a14a2add817c4b01651440de808371f78165ac90dc581'),
('owner8@clubhopper.com', 'Peter Davis', 'The Arcade', '555-6789', '4c1029697ee358715d3a14a2add817c4b01651440de808371f78165ac90dc581'),
('owner9@clubhopper.com', 'Katie Wilson', 'The Cellar', '555-1357', '4c1029697ee358715d3a14a2add817c4b01651440de808371f78165ac90dc581'),
('owner10@clubhopper.com', 'Mike Johnson', 'The Attic', '555-8642', '4c1029697ee358715d3a14a2add817c4b01651440de808371f78165ac90dc581'),
('q', 'Mike Johnson', 'The Attic', '555-8642', '8e35c2cd3bf6641bdb0e2050b76932cbb2e6034a0ddacc1d9bea82a6ba57f7cf');


-- PASSWORD: owner

------------------------------------------------------
CREATE TABLE clubs
(
	club_id int primary key IDENTITY(10000,1),
	OwnerEmail varchar(50) foreign key References ClubOwnerDetails(OwnerEmail),
	club_name Varchar(50),
	about varchar(200),
	Address1 varchar(80),
	Address2 varchar(80),
	postal_code varchar(80),
	city VARCHAR(50),
	country VARCHAR(50),
	Email varchar(50),
	Phone varchar(20),
	website VARCHAR(100),
	avgcost decimal(20),
	opening_time TIME,
	closing_time TIME,
	Ratings varchar(50),
	manager_name VARCHAR(50), 
	approval_status VARCHAR(1) DEFAULT 'N'
);


INSERT INTO clubs (
    OwnerEmail, club_name, about, Address1, Address2, postal_code, city, country, Email, Phone, website, avgcost, opening_time, closing_time, Ratings, manager_name
) VALUES 
    ('owner1@clubhopper.com', 'The Clubhouse', 'Legendary music venue located in downtown Toronto', '508 Queen St W', '', 'M5V 2B3', 'Toronto', 'Canada', 'info@velvet.ca', '+1 (416) 123-4567', 'www.velvet.ca', 20.00, '21:00:00', '02:00:00', '4.2', 'Jane Smith'),
    ('owner2@clubhopper.com', 'The Lounge', 'Multi-room nightclub with a waterfront patio', '11 Polson St', '', 'M5A 1A4', 'Toronto', 'Canada', 'info@rebeltoronto.com', '+1 (416) 469-5655', 'www.rebeltoronto.com', 30.00, '22:00:00', '03:00:00', '4.5', 'John Doe'),
    ('owner3@clubhopper.com', 'The Spot', 'Underground techno club in downtown Toronto', '794 Bathurst St', '', 'M5R 3G1', 'Toronto', 'Canada', 'info@codatoronto.com', '+1 (416) 536-0346', 'www.codatoronto.com', 25.00, '23:00:00', '04:00:00', '4.3', 'Sarah Johnson'),
    ('owner4@clubhopper.com', 'The Cave', 'Upscale nightclub with multiple levels and VIP booths', '15 Mercer St', '', 'M5V 2M9', 'Toronto', 'Canada', 'info@maisonmercer.com', '+1 (416) 341-8777', 'www.maisonmercer.com', 35.00, '22:00:00', '03:00:00', '4.1', 'Mike Smith'),
    ('owner5@clubhopper.com', 'The Hive', 'Modern nightclub with LED walls and a mezzanine', '473 Adelaide St W', '', 'M5V 1T1', 'Toronto', 'Canada', 'info@uniun.com', '+1 (416) 603-9300', 'www.uniun.com', 28.00, '22:00:00', '03:00:00', '4.4', 'Jessica Lee'),
    ('owner6@clubhopper.com', 'The Jazz Club', 'Vibrant nightclub with multiple rooms and dancefloors', '423 College St', '', 'M5T 1T1', 'Toronto', 'Canada', 'info@nest.to', '+1 (416) 792-9488', 'www.nest.to', 23.00, '22:00:00', '03:00:00', '4.2', 'David Kim'),
	('owner7@clubhopper.com', 'The Rooftop', 'A luxurious lounge with VIP bottle service and live music', '101 Yorkville Ave', NULL, 'M5R 1C1', 'Toronto', 'Canada', 'info@thevelvetroom.com', '+1-416-555-3456', 'www.thevelvetroom.com', 100.00, '20:00:00', '02:00:00', '4.8', 'Emily Wong'),
('owner8@clubhopper.com', 'The Arcade', 'A popular nightclub that features live DJs and multiple dance floors', '11 Polson St', NULL, 'M5A 1A4', 'Toronto', 'Canada', 'info@thewarehouse.com', '+1-416-555-7890', 'www.thewarehouse.com', 50.00, '22:00:00', '03:00:00', '4.6', 'David Lee'),
('owner9@clubhopper.com', 'The Cellar', 'A stylish lounge with a chic decor and delicious cocktails', '222 Richmond St W', NULL, 'M5V 1W4', 'Toronto', 'Canada', 'info@theden.com', '+1-416-555-2345', 'www.theden.com', 80.00, '19:00:00', '02:00:00', '4.3', 'Sarah Kim'),
('owner10@clubhopper.com', 'The Attic', 'A cozy rooftop bar with a stunning view of the city', '333 King St E', 'Floor 5', 'M5A 1L1', 'Toronto', 'Canada', 'info@theattic.com', '+1-416-555-6789', 'www.theattic.com', 60.00, '17:00:00', '02:00:00', '4.1', 'Alex Chen'),
('q', 'The Hive', 'A cozy bar that serves craft beers and cocktails', '789 King St W', NULL, 'M5V 1N4', 'Toronto', 'Canada', 'info@thehive.com', '+1-416-555-9012', 'www.thehive.com', 40.00, '18:00:00', '02:00:00', '4.0', 'Mike Johnson');


Create Table Admin
(
email varchar(100) primary Key,
phone varchar(20)NOT NULL,
password VARCHAR(64) NOT NULL,
);

INSERT INTO ADMIN VALUES('1','1','1');

INSERT INTO ADMIN VALUES('admin@clubhopper.ca','1234512345','admin123');









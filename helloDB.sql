CREATE SCHEMA helloDB;

USE helloDB;

CREATE TABLE Users (
	userID INTEGER AUTO_INCREMENT NOT NULL,
	user_type ENUM('User', 'Vendor') NOT NULL,
	name VARCHAR(255) NOT NULL,
	birthdate DATETIME NOT NULL,
	email VARCHAR(255) NOT NULL,
	PRIMARY KEY(userID),
	KEY(userID, user_type)
	);

CREATE TABLE Addresses (
	addressID INTEGER AUTO_INCREMENT NOT NULL,
	userID INTEGER NOT NULL,
	name VARCHAR(255) NOT NULL,
	phone DECIMAL(11,0),
	streetAddr VARCHAR(255) NOT NULL,
	city VARCHAR(255) NOT NULL,
	state CHAR(2) NOT NULL,
	zip DECIMAL(5,0) NOT NULL,
	zip_ext DECIMAL(4,0),
	PRIMARY KEY (addressID),
	FOREIGN KEY (userID) REFERENCES Users(userID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
	);
	
CREATE TABLE Vendors (
	userID INTEGER NOT NULL,
	user_type ENUM('User', 'Vendor') NOT NULL,
	company_name VARCHAR(255) NOT NULL,
	PRIMARY KEY(userID),
	FOREIGN KEY(userID, user_type) REFERENCES Users(userID, user_type), 
    CONSTRAINT is_vendor CHECK(user_type='Vendor')
	);
	
CREATE TABLE Categories (
	name VARCHAR(30) NOT NULL, 
	description VARCHAR(2000), 
	parent VARCHAR(30), 
	PRIMARY KEY(name), 
	FOREIGN KEY(parent) REFERENCES Categories (name) 
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT tree_constraint CHECK(name = "All" XOR (parent <> NULL))
	);
	
CREATE TABLE Items (
	itemID INTEGER AUTO_INCREMENT NOT NULL,
	name VARCHAR(255) NOT NULL,
	category VARCHAR(30) NOT NULL,
	PRIMARY KEY(itemID),
	FOREIGN KEY(category) REFERENCES Categories(name)
		ON UPDATE CASCADE
	);
	
CREATE TABLE Transactions (
	seller_userID INTEGER NOT NULL,
	buyer_userID INTEGER NOT NULL,
	timestamp DATETIME NOT NULL,
	itemID INTEGER NOT NULL,
	itemCt INTEGER UNSIGNED NOT NULL,
	carrier_trackingNum VARCHAR(255),
	salePrice DECIMAL(6,2) NOT NULL,
	PRIMARY KEY(seller_userID, buyer_userID, itemID, timestamp),
	FOREIGN KEY(seller_userID) REFERENCES Users (userID),
	FOREIGN KEY(buyer_userID) REFERENCES Users (userID),
	FOREIGN KEY(itemID) REFERENCES Items (itemID)
	);
	
CREATE TABLE Ratings (
	seller_userID INTEGER NOT NULL,
	buyer_userID INTEGER NOT NULL,
	timestamp DATETIME NOT NULL,
	itemID INTEGER NOT NULL,
	subject VARCHAR(255) NOT NULL,
	rating TINYINT NOT NULL,
	content VARCHAR(2000) NOT NULL,
	CONSTRAINT star_rating CHECK (rating >= 0 AND rating <=5),
	PRIMARY KEY(seller_userID, buyer_userID, itemID, timestamp),
	FOREIGN KEY(seller_userID, buyer_userID, itemID, timestamp) REFERENCES Transactions(seller_userID, buyer_userID, itemID, timestamp)
	);
	
CREATE TABLE Reviews (
	itemID INTEGER NOT NULL,
	author_userID INTEGER NOT NULL,
	rating TINYINT NOT NULL, 
	CONSTRAINT star_rating CHECK (rating >= 0 AND rating <=5),
	content VARCHAR(2000) NOT NULL, 
	timestamp DATETIME NOT NULL, 
	PRIMARY KEY (itemID, author_userID), 
	FOREIGN KEY (itemID) REFERENCES Items (itemID)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	FOREIGN KEY (author_userID) REFERENCES Users(userID)
		ON DELETE CASCADE
		ON UPDATE CASCADE
	);
	
CREATE TABLE Sells (
	itemID INTEGER NOT NULL, 
	sellerID INTEGER NOT NULL,
	description VARCHAR(2000) NOT NULL, 
	price DECIMAL(6,2) NOT NULL,
	PRIMARY KEY(itemID, sellerID), 
	FOREIGN KEY(itemID) REFERENCES Items(itemID)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	FOREIGN KEY(sellerID) REFERENCES Users(userID)
		ON DELETE CASCADE
		ON UPDATE CASCADE
	);
	
CREATE TABLE Auctions (
	auctioneerID INTEGER NOT NULL,
	itemID INTEGER NOT NULL,
	description VARCHAR(2000) NOT NULL,
	reserve_price DECIMAL(6,2) NOT NULL,
	start_time DATETIME NOT NULL,
	end_time DATETIME NOT NULL, 
	PRIMARY KEY(auctioneerID, start_time),
	FOREIGN KEY(auctioneerID) REFERENCES Users(userID)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	FOREIGN KEY(itemID) REFERENCES Items(itemID)
		ON DELETE CASCADE
		ON UPDATE CASCADE
	);
	
CREATE TABLE Bids (
	bidderID INTEGER NOT NULL,
	auctioneerID INTEGER NOT NULL,
	itemID INTEGER NOT NULL,
	auction_start DATETIME NOT NULL,
	timestamp DATETIME NOT NULL, 
	amount DECIMAL(6,2), 
	PRIMARY KEY (bidderID, auctioneerID, auction_start), 
	FOREIGN KEY (auctioneerID, auction_start) REFERENCES Auctions(auctioneerID, start_time)
		ON DELETE CASCADE
		ON UPDATE CASCADE
	
	);
	
CREATE TABLE CreditCards (
	userID INTEGER NOT NULL,
	ccv INTEGER NOT NULL, 
	addressID INTEGER NOT NULL,
	merchant VARCHAR(20) NOT NULL, 
	ccNumber DECIMAL(16,0) NOT NULL, 
	exp_date DATE, 
	PRIMARY KEY(ccNumber),
	FOREIGN KEY(userID) REFERENCES Users(userID)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	FOREIGN KEY(addressID) REFERENCES Addresses(addressID)
	);
    
    
LOAD DATA LOCAL INFILE 'C:/Users/Frank/Documents/GitHub/cmpsc431w-group-work/csv/Users.csv' 
INTO TABLE Users
FIELDS TERMINATED BY ', ' 
ENCLOSED BY '\''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/Users/Frank/Documents/GitHub/cmpsc431w-group-work/csv/Addresses.csv' 
INTO TABLE Addresses
FIELDS TERMINATED BY ', ' 
ENCLOSED BY '\''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/Users/Frank/Documents/GitHub/cmpsc431w-group-work/csv/Vendors.csv' 
INTO TABLE Vendors
FIELDS TERMINATED BY ', ' 
ENCLOSED BY '\''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/Users/Frank/Documents/GitHub/cmpsc431w-group-work/csv/Categories.csv' 
INTO TABLE Categories
FIELDS TERMINATED BY ', ' 
ENCLOSED BY '\''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/Users/Frank/Documents/GitHub/cmpsc431w-group-work/csv/Items.csv' 
INTO TABLE Items
FIELDS TERMINATED BY ', ' 
ENCLOSED BY '\''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/Users/Frank/Documents/GitHub/cmpsc431w-group-work/csv/Transactions.csv' 
INTO TABLE Transactions
FIELDS TERMINATED BY ', ' 
ENCLOSED BY '\''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/Users/Frank/Documents/GitHub/cmpsc431w-group-work/csv/Ratings.csv' 
INTO TABLE Ratings
FIELDS TERMINATED BY ', ' 
ENCLOSED BY '\''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/Users/Frank/Documents/GitHub/cmpsc431w-group-work/csv/Reviews.csv' 
INTO TABLE Reviews
FIELDS TERMINATED BY ', ' 
ENCLOSED BY '\''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/Users/Frank/Documents/GitHub/cmpsc431w-group-work/csv/Sells.csv' 
INTO TABLE Sells
FIELDS TERMINATED BY ', ' 
ENCLOSED BY '\''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/Users/Frank/Documents/GitHub/cmpsc431w-group-work/csv/Auctions.csv' 
INTO TABLE Auctions
FIELDS TERMINATED BY ', ' 
ENCLOSED BY '\''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/Users/Frank/Documents/GitHub/cmpsc431w-group-work/csv/Bids.csv' 
INTO TABLE Bids
FIELDS TERMINATED BY ', ' 
ENCLOSED BY '\''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/Users/Frank/Documents/GitHub/cmpsc431w-group-work/csv/CreditCards.csv' 
INTO TABLE CreditCards
FIELDS TERMINATED BY ', ' 
ENCLOSED BY '\''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
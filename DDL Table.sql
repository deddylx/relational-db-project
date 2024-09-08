CREATE TABLE city(
	city_id int PRIMARY KEY,
	city_name varchar(100) NOT NULL,
	latitude decimal NOT NULL,
	longitude decimal NOT NULL
);

CREATE TABLE users(
	user_id integer PRIMARY KEY,
	username varchar(100) NOT NULL,
	name varchar(100) NOT NULL,
	email varchar(100) NOT NULL UNIQUE,
	phone_number varchar(50) NOT NULL,
	address varchar(100) NOT NULL,
	city_id integer NOT NULL,
	password varchar(100) NOT NULL CHECK(LENGTH(password) >= 8),
	created_at timestamp NOT NULL,
	CONSTRAINT fk_city_id
		FOREIGN KEY(city_id)
		REFERENCES city(city_id)
		ON DELETE RESTRICT
);

CREATE TABLE product_ads(
	ad_id integer PRIMARY KEY,
	user_id integer,
	title varchar(100) NOT NULL,
	can_bid boolean DEFAULT FALSE NOT NULL,
	created_at timestamp NOT NULL,
	CONSTRAINT fk_user_id
		FOREIGN KEY(user_id)
		REFERENCES users(user_id)
		ON DELETE NO ACTION
);

CREATE TABLE product_detail(
	product_id integer PRIMARY KEY,
	ad_id integer UNIQUE,
	brand varchar(50) NOT NULL,
	model varchar(100) NOT NULL,
	body_type varchar(100) NOT NULL,
	transmission_type varchar(50) NOT NULL,
	year varchar(4) NOT NULL,
	description varchar(500),
	price numeric NOT NULL,
	CONSTRAINT fk_ad_id
		FOREIGN KEY(ad_id)
		REFERENCES product_ads(ad_id)
		ON DELETE CASCADE
);

CREATE TABLE bids(
	bid_id integer PRIMARY KEY,
	ad_id integer,
	buyer_id integer,
	bid_price numeric NOT NULL,
	created_at timestamp NOT NULL,
	CONSTRAINT fk_ad_id
		FOREIGN KEY(ad_id)
		REFERENCES product_ads(ad_id)
		ON DELETE CASCADE,
	CONSTRAINT fk_buyer_id
		FOREIGN KEY(buyer_id)
		REFERENCES users(user_id)
		ON DELETE NO ACTION
);
		
ALTER TABLE product_detail
	ADD CONSTRAINT price_check
		CHECK(price >= 0);
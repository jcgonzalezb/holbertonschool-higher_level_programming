-- Creates the the database hbtn_0d_usa and the table cities.
-- description: id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null and is a foreign key that references to id of the states table
-- name VARCHAR(256) can’t be null.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
	state_id INT IDENTITY(1,1) NOT NULL,
	name VARCHAR(256) NOT NULL
	FOREIGN KEY (id) REFERENCES states (id)
);

-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database for use
USE hbtn_0d_usa;

-- Create the 'states' table if it doesn't already exist
CREATE TABLE IF NOT EXISTS states
(
    -- 'id' column as primary key with automatic increment
    id INT PRIMARY KEY AUTO_INCREMENT,
    
    -- 'name' column for state name, required (cannot be NULL)
    name VARCHAR(256) NOT NULL
);

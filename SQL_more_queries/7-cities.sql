-- Create the database 'hbtn_0d_usa' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the 'hbtn_0d_usa' database
USE hbtn_0d_usa;

-- Create the 'cities' table if it doesn't already exist
CREATE TABLE IF NOT EXISTS cities (
    -- 'id' column as primary key with automatic increment
    id INT PRIMARY KEY AUTO_INCREMENT,
    
    -- 'state_id' column to reference the 'states' table, required (cannot be NULL)
    state_id INT NOT NULL,
    
    -- 'name' column for the city name, required (cannot be NULL)
    name VARCHAR(256) NOT NULL,
    
    -- Define 'state_id' as a foreign key that references the 'id' column in the 'states' table
    FOREIGN KEY (state_id) REFERENCES states(id)
);

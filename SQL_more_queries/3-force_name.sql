-- a script that creates the table force_name
-- If the table force_name already exists, your script should not fail
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

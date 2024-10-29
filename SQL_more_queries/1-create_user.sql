-- This script creates a MySQL user 'user_0d_1' with all privileges
-- withThe password for the user is set to 'user_0d_1_pwd'
-- If the user already exists, the script will not fail
-- The script also lists the privileges of 'user_0d_1' and 'user_0d_2' on the server*/
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;

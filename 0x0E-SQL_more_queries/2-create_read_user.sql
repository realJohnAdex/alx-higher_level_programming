-- creates the MySQL server user user_0d_2 and db hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- If user user_0d_2 does not exist, create it
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant select privileges to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

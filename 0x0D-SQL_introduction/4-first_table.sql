-- creates a table called first_table in current db in MySQL server
-- If the table already exists, the script will not fail
-- SELECT or SHOW statements not allowed
CREATE TABLE IF NOT EXISTS first_table(id INT, name VARCHAR(256));

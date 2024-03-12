-- prints the full description first_table from the db hbtn_0c_0
-- database name will be passed as an argument of the mysql
-- DESCRIBE or EXPLAIN statements not allowed
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

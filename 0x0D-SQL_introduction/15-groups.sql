-- lists all rows of the table first_table from the db hbtn_0c_0
-- All fields should be printed
-- db name will be passed as an argument of the mysql command
SELECT score, COUNT(*) AS number FROM second_table  GROUP BY score;

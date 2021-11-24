-- Lists the number of records with the same score
-- in the table second_table of the database hbtn_0c_0.

SELECT COUNT(*) as number, score
FROM second_table
GROUP BY score
HAVING number > 1
ORDER BY number DESC;

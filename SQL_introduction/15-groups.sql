-- a script that lists the number of records with the same score 
SELECT score, COUNT(*) AS number
FROM second_table
-- result displaed by score
GROUP BY score
--  list sorted by the number of records (descending)
ORDER BY number DESC;

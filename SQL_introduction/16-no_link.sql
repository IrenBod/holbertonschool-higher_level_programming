UPDATE hbtn_0c_0.second_table
SET name = NULL
WHERE id = 4;

INSERT INTO hbtn_0c_0.second_table (id, name, score)
VALUES
(5, "Aria", 18),
(6, "Aria", 12);

SELECT score, name FROM hbtn_0c_0.second_table
WHERE name IS NOT NULL
GROUP BY score, name
ORDER BY score DESC, name;

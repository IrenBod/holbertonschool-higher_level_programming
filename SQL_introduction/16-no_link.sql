UPDATE second_table
SET name = NULL
WHERE id = 4;

INSERT INTO second_table (id, name, score)
VALUES
(5, "Aria", 18),
(6, "Aria", 12);

SELECT score, name FROM second_table
WHERE name IS NOT NULL
GROUP BY score, name
ORDER BY score DESC, name;
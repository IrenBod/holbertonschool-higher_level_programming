-- Select city id and name from the cities table
SELECT cities.id, cities.name
FROM cities
-- Filter cities by state_id that matches the id of California in the states table
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
-- Sort results by city id in ascending order
ORDER BY cities.id ASC;


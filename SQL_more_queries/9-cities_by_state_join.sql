-- Select columns 'id' and 'name' from 'cities' table and 'name' from 'states' table
SELECT cities.id, cities.name, states.name
FROM cities

-- Join 'cities' and 'states' tables based on matching 'state_id' in 'cities' and 'id' in 'states'
JOIN states ON cities.state_id = states.id

-- Sort results by 'id' in ascending order
ORDER BY cities.id ASC;

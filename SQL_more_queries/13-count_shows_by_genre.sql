-- Select 'name' from 'tv_genres' table as 'genre' and count of 'show_id' from 'tv_show_genres' table as 'number_of_shows'
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres

-- Join 'tv_genres' and 'tv_show_genres' tables where 'id' in 'tv_genres' matches 'genre_id' in 'tv_show_genres'
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id

-- Group results by genre name to count the number of shows for each genre
GROUP BY tv_genres.name

-- Filter to include only genres with one or more linked shows
HAVING number_of_shows > 0

-- Sort results in descending order by the number of shows linked to each genre
ORDER BY number_of_shows DESC;

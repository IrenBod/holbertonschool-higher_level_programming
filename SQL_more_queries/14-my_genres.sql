-- Select 'name' from 'tv_genres' table to display genres associated with the show 'Dexter'
SELECT tv_genres.name
FROM tv_genres

-- Join 'tv_genres' and 'tv_show_genres' tables where 'id' in 'tv_genres' matches 'genre_id' in 'tv_show_genres'
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id

-- Join 'tv_show_genres' and 'tv_shows' tables where 'show_id' in 'tv_show_genres' matches 'id' in 'tv_shows'
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id

-- Filter results to include only genres associated with the show titled 'Dexter'
WHERE tv_shows.title = 'Dexter'

-- Sort results in ascending order by genre name
ORDER BY tv_genres.name ASC;

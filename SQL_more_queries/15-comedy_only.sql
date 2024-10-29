-- Select 'title' from 'tv_shows' table to display titles of shows associated with the genre 'Comedy'
SELECT tv_shows.title
FROM tv_shows

-- Join 'tv_shows' and 'tv_show_genres' tables where 'id' in 'tv_shows' matches 'show_id' in 'tv_show_genres'
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id

-- Join 'tv_show_genres' and 'tv_genres' tables where 'genre_id' in 'tv_show_genres' matches 'id' in 'tv_genres'
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id

-- Filter results to include only shows associated with the genre named 'Comedy'
WHERE tv_genres.name = 'Comedy'

-- Sort results in ascending order by show title
ORDER BY tv_shows.title ASC;


-- Select 'title' from 'tv_shows' table and 'genre_id' from 'tv_show_genres' table
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows

-- Left join 'tv_shows' and 'tv_show_genres' tables, including all 'tv_shows' records even if no matching 'show_id' is found in 'tv_show_genres'
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id

-- Filter results to include only those shows with no linked genre (where 'genre_id' is NULL)
WHERE tv_show_genres.genre_id IS NULL

-- Sort results by 'title' in ascending order
ORDER BY tv_shows.title ASC;

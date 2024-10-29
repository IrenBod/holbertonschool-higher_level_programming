-- Select 'title' from 'tv_shows' table and 'genre_id' from 'tv_show_genres' table
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows

-- Left join 'tv_shows' and 'tv_show_genres' tables, including all 'tv_shows' records even if no matching 'show_id' is found in 'tv_show_genres'
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id

-- Sort results by 'title' in ascending order, and then by 'genre_id' in ascending order
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

-- Select 'title' from 'tv_shows' table and 'name' from 'tv_genres' table, renaming it as 'genre'
SELECT tv_shows.title, tv_genres.name AS genre
FROM tv_shows

-- Left join 'tv_shows' and 'tv_show_genres' tables to include all shows, even those without a genre
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id

-- Left join 'tv_show_genres' and 'tv_genres' tables to include genre names where available, otherwise NULL
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id

-- Sort results in ascending order by show title, and then by genre name
ORDER BY tv_shows.title ASC, tv_genres.name ASC;

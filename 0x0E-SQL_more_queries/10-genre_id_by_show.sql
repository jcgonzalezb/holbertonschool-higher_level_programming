-- Lists all shows contained in hbtn_0d_tvshows that have
-- at least one genre linked.
-- Display: tv_shows.title - tv_show_genres.genre_id.
-- Ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM cities, states
WHERE tv_show_genres.genre_id >= 1
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;

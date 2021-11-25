-- Lists all shows contained in hbtn_0d_tvshows.
-- Display: tv_shows.title - tv_show_genres.genre_id.
-- If a show doesn’t have a genre, display NULL.
-- Ascending order by tv_shows.title and tv_show_genres.genre_id

   SELECT tv_shows.title, tv_show_genres.genre_id
     FROM tv_shows
LEFT JOIN tv_show_genres
       ON tv_show_genres.show_id = tv_shows.id
 ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;

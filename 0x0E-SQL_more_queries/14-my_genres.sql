-- Lists all genres of the show Dexter.
-- The tv_shows table contains only one record where
-- title = Dexter (but the id can be different).
-- Each record should display: tv_genres.name.
-- Results must be sorted in ascending order by the genre name.

SELECT tv_genres.name
FROM tv_genres
RIGHT JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.show_id = 8
ORDER BY tv_genres ASC;

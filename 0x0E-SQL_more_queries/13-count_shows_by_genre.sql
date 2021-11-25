-- Lists all genres from hbtn_0d_tvshows and displays the number of
-- shows linked to each.
-- Display: <TV Show genre> - <Number of shows linked to this genre>.
-- First column must be called genre. Second column must be called number_of_shows.
-- Don’t display a genre that doesn’t have any shows linked.
-- Results must be sorted in descending order by the number of shows linked.

SELECT tv_genres.name AS genre, COUNT (tv_shows.title) as number_of_shows
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_show
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name IS NOT NULL
GROUP BY tv_genres.name
ORDER BY number_of_shows DES;

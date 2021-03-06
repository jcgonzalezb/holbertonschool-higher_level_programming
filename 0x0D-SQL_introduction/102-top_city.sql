-- Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

SELECT city, AVG(value) AS avg_temp
from temperatures
WHERE month between 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

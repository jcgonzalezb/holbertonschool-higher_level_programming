-- Lists all cities contained in the database hbtn_0d_usa.

SELECT id, name
FROM cities
WHERE state_id = 1
ORDER BY name ASC;

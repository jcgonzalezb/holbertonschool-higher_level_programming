-- Lists all the cities of California that can be found in the database hbtn_0d_usa.
-- The states table contains only one record where name = California.
-- Results must be sorted in ascending order by cities.id

SELECT hbtn_0d_usa.cities.id, hbtn_0d_usa.cities.name
FROM hbtn_0d_usa.cities, hbtn_0d_usa.states
WHERE hbtn_0d_usa.states.id = hbtn_0d_usa.cities.state_id

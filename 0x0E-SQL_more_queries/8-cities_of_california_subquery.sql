-- Lists all the cities of California that can be found in the database hbtn_0d_usa.
-- The states table contains only one record where name = California.
-- Results must be sorted in ascending order by cities.id

SELECT cities.id, cities.name
  FROM cities, states
 WHERE states.id = 1 AND cities.state_id = 1;

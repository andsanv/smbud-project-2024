MATCH (d:Crew)-[:WORKED_IN {role: 'Director'}]-(m:Movie)
WHERE m.rating IS NOT NULL
WITH d.name as DIRECTOR, avg(m.rating) as AVG_RATING, COUNT(m) as N_MOVIES
RETURN DIRECTOR, AVG_RATING, N_MOVIES
ORDER BY AVG_RATING * log(log(N_MOVIES+1)) DESC
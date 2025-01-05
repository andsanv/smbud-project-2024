MATCH (m:Movie)
WHERE m.duration >= 60 AND m.release_date < 2024
WITH m.release_date AS YEAR, avg(m.rating) AS AVG_RATING, avg(m.duration) AS AVG_DURATION, count(m) AS N_MOVIES
RETURN YEAR, AVG_RATING, AVG_DURATION, N_MOVIES
ORDER BY YEAR DESC;

MATCH (m:Movie)-[:FILMED_IN]->(c:Country)
WHERE m.release_date >= 1900 AND m.release_date <= 2023 AND m.rating >= 3.8
WITH m.release_date AS year, c.name AS country, count(m) AS movie_count
RETURN year, country, movie_count
ORDER BY year DESC, movie_count DESC;

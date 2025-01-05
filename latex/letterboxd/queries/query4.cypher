MATCH (s:Studio)-[:HAS_PRODUCED]->(m:Movie)
WHERE m.release_date >= 1900 AND m.release_date <= 2023 AND m.rating >= 3
WITH s.name AS studio, m.release_date AS year, count(m) AS movies_count
ORDER BY year DESC, movies_count DESC
WITH year, COLLECT({studio: studio, movies_count: movies_count}) AS studios
UNWIND range(0, 4) AS idx
WITH year, studios[idx] AS studio_info
RETURN year, studio_info.studio AS studio, studio_info.movies_count AS movies_count
ORDER BY year DESC, movies_count DESC

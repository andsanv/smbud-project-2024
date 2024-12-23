MATCH (m:Movie)-[:BELONGS_TO_GENRE]->(g:Genre)
WHERE m.release_date >= 1900 AND m.release_date <= 2023 AND m.rating >= 3
WITH m.release_date as year, g.name as genre, count(*) as cnt
RETURN year, genre, cnt
ORDER BY year DESC, cnt DESC

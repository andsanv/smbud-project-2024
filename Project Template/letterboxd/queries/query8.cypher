MATCH (a:Actor)-[:ACTED_IN]->(m:Movie)-[:BELONGS_TO_GENRE]->(g:Genre)
WHERE m.release_date >= 2000 AND m.release_date <= 2024 AND m.rating >= 3.5 AND g.name <> "Documentary" AND g.name <> "Music"
WITH a.name AS actor, g.name AS genre, COUNT(*) AS appearances
RETURN actor, genre, appearances
ORDER BY appearances DESC
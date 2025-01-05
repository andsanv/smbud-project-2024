MATCH (a:Actor)-[:ACTED_IN]->(m:Movie)-[:BELONGS_TO_GENRE]->(g:Genre), (m)-[:FILMED_IN]-(:Country {name: "USA"})
WHERE m.release_date >= 2000 AND m.release_date <= 2024 AND m.rating >= 3.5 AND g.name <> "Documentary" AND g.name <> "Music" AND g.name <> "Animation"
WITH a.name AS actor, g.name AS genre, COUNT(distinct m) AS appearances
RETURN actor, genre, appearances
ORDER BY appearances DESC
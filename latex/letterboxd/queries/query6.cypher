MATCH (a:Actor)-[:ACTED_IN]->(m:Movie)-[:FILMED_IN]->(:Country {name: "USA"}), (m)-[:BELONGS_TO_GENRE]->(g:Genre)
WHERE m.release_date >= 2000 AND m.release_date <= 2024 AND m.rating is not null AND g.name <> "Documentary" AND g.name <> "Music"
WITH a.name as actor, avg(m.rating) as rating, COUNT(distinct m) as cnt
WHERE cnt >= 20
RETURN actor, rating, cnt
ORDER BY rating DESC
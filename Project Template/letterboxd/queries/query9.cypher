MATCH (m:Movie)-[:BELONGS_TO_GENRE]->(g:Genre), (m)-[:FILMED_IN]-(:Country {name: "USA"})
WHERE m.release_date >= 1900 AND m.release_date <= 2024 AND m.rating >= 3.5 AND g.name <> "Documentary" AND g.name <> "Music"
MATCH (m)<-[w:WORKED_IN {role: "Director"}]-(d:Crew)
MATCH (a:Actor)-[r:ACTED_IN]->(m)
WITH a.name AS actor, d.name AS director, count(m) AS cnt
RETURN actor, director, cnt
ORDER BY cnt DESC;
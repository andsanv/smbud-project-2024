MATCH (m:Movie)-[:BELONGS_TO_GENRE]->(g:Genre), 
      (m)-[:FILMED_IN]-(:Country {name: "USA"})
WHERE m.release_date >= 1900 AND m.release_date <= 2024 
  AND m.rating >= 4
WITH m, collect(g.name) AS genres
WHERE NONE(genre IN genres WHERE genre IN ["Documentary", "Music", "Animation"])
MATCH (m)<-[w:WORKED_IN {role: "Director"}]-(d:Crew)
MATCH (a:Actor)-[r:ACTED_IN]->(m)
WITH a.name AS actor, d.name AS director, count(m) AS cnt
RETURN actor, director, cnt
ORDER BY cnt DESC;

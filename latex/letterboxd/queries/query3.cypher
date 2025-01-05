MATCH (m:Movie)-[:BELONGS_TO_GENRE]->(g:Genre)
WITH g.name AS genre, avg(m.rating) AS rating
RETURN genre, rating
ORDER BY rating DESC
Match (m:Movie)-[:BELONGS_TO_GENRE]->(g:Genre)
with g.name as genre, avg(m.rating) as rating
return genre, rating
order by rating desc
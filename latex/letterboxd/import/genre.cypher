:auto
LOAD CSV WITH HEADERS FROM 'file:///genres.csv' AS row
CALL(row) {
MATCH (m:Movie {id: toInteger(row.id)})
MERGE (g:Genre {name: row.genre})
CREATE (g)<-[:BELONGS_TO_GENRE]-(m)
} IN TRANSACTIONS;
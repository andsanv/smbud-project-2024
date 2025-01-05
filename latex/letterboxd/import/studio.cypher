:auto
LOAD CSV WITH HEADERS FROM 'file:///studios.csv' AS row
CALL(row) {
MATCH (m:Movie {id: toInteger(row.id)})
MERGE (s:Studio {name: row.studio})
CREATE (s)-[:HAS_PRODUCED]->(m)
} IN TRANSACTIONS;
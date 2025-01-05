:auto
LOAD CSV WITH HEADERS FROM 'file:///countries.csv' AS row
CALL(row) {
MATCH (m:Movie {id: toInteger(row.id)})
MERGE (c:Country {name: row.country})
CREATE (c)<-[:FILMED_IN]-(m)
} IN TRANSACTIONS;
:auto
LOAD CSV WITH HEADERS FROM 'file:///themes.csv' AS row
CALL(row) {
MATCH (m:Movie {id: toInteger(row.id)})
MERGE (t:Theme {name: row.theme})
CREATE (t)<-[:ABOUT]-(m)
} IN TRANSACTIONS;
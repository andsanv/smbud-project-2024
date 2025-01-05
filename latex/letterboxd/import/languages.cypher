:auto
LOAD CSV WITH HEADERS FROM 'file:///languages.csv' AS row
CALL(row) {
MATCH (m:Movie {id: toInteger(row.id)})
MERGE (l:Language {name: row.language})
CREATE (l)<-[:SPOKEN_IN {type: row.type}]-(m)
} IN TRANSACTIONS;
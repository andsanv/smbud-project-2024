:auto
LOAD CSV WITH HEADERS FROM 'file:///crew.csv' AS row
CALL(row) {
MATCH (m:Movie {id: toInteger(row.id)})
MERGE (c:Crew {name: row.name})
CREATE (c)-[:WORKED_IN {role: row.role}]->(m)
} IN TRANSACTIONS;
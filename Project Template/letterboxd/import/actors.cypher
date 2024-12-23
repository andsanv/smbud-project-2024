:auto
LOAD CSV WITH HEADERS FROM 'file:///actors.csv' AS row
CALL(row) {
MATCH (m:Movie {id: toInteger(row.id)})
MERGE (a:Actor {name: row.name})
CREATE (a)-[:ACTED_IN {role: row.role}]->(m)
} IN TRANSACTIONS;
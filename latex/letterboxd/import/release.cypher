:auto
LOAD CSV WITH HEADERS FROM 'file:///releases.csv' AS row
CALL(row) {
MATCH (m:Movie {id: toInteger(row.id)}), (c:Country {name: row.country})
CREATE (c)<-[:RELEASED_IN {type: row.type, rating: row.rating, realeasedIn: date(row.date)}]-(m)
} IN TRANSACTIONS;
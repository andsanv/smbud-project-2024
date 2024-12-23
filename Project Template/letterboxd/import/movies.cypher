:auto
LOAD CSV WITH HEADERS FROM 'file:///movies.csv' AS row
CALL(row) {
CREATE (:Movie {
id: toInteger(row.id),
name: row.name,
release_date: toInteger(row.date),
tagline: row.tagline,
description: row.description,
duration: toInteger(row.minute),
rating: toFloat(row.rating)
})
} IN TRANSACTIONS
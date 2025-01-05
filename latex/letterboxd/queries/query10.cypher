MATCH (m:Movie)-[r:RELEASED_IN]->(c:Country)
WHERE r.type IN ["Theatrical", "Digital"] AND m.release_date = date(r.realeasedIn).year AND date(r.realeasedIn).year <= 2023
WITH date(r.realeasedIn).year AS releaseYear, r.type AS releaseType, COUNT(DISTINCT m) AS totalMovies
RETURN releaseYear, releaseType, totalMovies
ORDER BY releaseYear DESC, totalMovies DESC
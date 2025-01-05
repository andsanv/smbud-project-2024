query = collection.aggregate([
    { "$unwind": { "path": "$weekends" } },
    { "$unwind": { "path": "$weekends.race.results" } },
    { "$match": { "weekends.race.results.position": 1 } },
    {
        "$group": {
            "_id": {"grid": "$weekends.race.results.grid"},
            "wins": {"$sum": 1}
        }
    },
    { "$sort": {"_id.grid": 1} },
    {
        "$project": {
            "_id": 0,
            "Grid": "$_id.grid",
            "Wins Count": "$wins"
        }
    }
])
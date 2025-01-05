query = collection.aggregate([
    { "$unwind": { "path": "$weekends" } },
    { "$unwind": { "path": "$weekends.race.results" } },
    { "$match": { "weekends.race.results.position": 1 } },
    {
        "$group": {
            "_id": {"driver": "$weekends.race.results.car.driver"},
            "wins": {"$sum": 1}
        }
    },
    { "$sort": {"wins": -1} },
    { "$limit": 10 },
    {
        "$project": {
            "_id": 0,
            "Name": "$_id.driver.name",
            "Surname": "$_id.driver.surname",
            "Wins": "$wins",
        }
    }
])
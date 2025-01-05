query = collection.aggregate([
    { "$unwind": { "path": "$weekends" } },
    { "$unwind": { "path": "$weekends.race.results" } },
    {
        "$match": {
            "weekends.race.results.car.constructor.name": "Ferrari"
        }
    },
    {
        "$group": {
            "_id": {"driver": "$weekends.race.results.car.driver"},
            "wins": {
                "$sum": {
                    "$cond": { "if": { "$eq": ["$weekends.race.results.position", 1] }, "then": 1, "else": 0 }
                }
            },
            "races": {"$sum": 1}
        }
    },
    {
        "$project": {
            "_id": 0,
            "Name": "$_id.driver.name",
            "Surname": "$_id.driver.surname",
            "Wins": "$wins",
            "Races": "$races",
        }
    },
    { "$sort": {"Races": -1} },
    { "$limit": 15 }
])
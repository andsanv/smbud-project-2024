query = collection.aggregate([
    { "$unwind": { "path": "$weekends" } },
    { "$addFields": { "first_result": "$weekends.race.results" } },
    {
        "$project": {
            "first_result": 1,
            "second_result": "$weekends.race.results"
        }
    },
    { "$unwind": { "path": "$first_result" } },
    { "$unwind": { "path": "$second_result" } },
    {
        "$match": {
            "$expr": {
                "$and": [
                    { "$ne": ["$first_result.car.driver", "$second_result.car.driver"] },
                    { "$eq": ["$first_result.car.constructor", "$second_result.car.constructor"] }
                ]
            }
        }
    },
    {
        "$group": {
            "_id": {"driver": "$first_result.car.driver"},
            "wins": {
                "$sum": {
                    "$cond": { "if": { "$lt": ["$first_result.order", "$second_result.order"] }, "then": 1, "else": 0 }
                }
            },
            "duels": {"$sum": 1}
        }
    },
    {
        "$project": {
            "driver": "$_id.driver",
            "wins": "$wins",
            "duels": "$duels",
            "wins_percentage": { "$divide": ["$wins", "$duels"] }
        }
    },
    { "$sort": { "wins_percentage": -1 } },
    { "$match": {"duels": { "$gt": 100 }} },
    { "$limit": 10 },
    {
        "$project": {
            "_id": 0,
            "Name": "$_id.driver.name",
            "Surname": "$_id.driver.surname",
            "Wins": "$wins",
            "Duels Count": "$duels",
            "Win Percentage": "$wins_percentage",
        }
    }
])
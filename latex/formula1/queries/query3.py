query = collection.aggregate([
    { "$unwind": {"path": "$weekends"} },
    { "$unwind": {"path": "$weekends.race.results"} },
    { "$match": {"weekends.race.results.position": 1} },
    {
        "$group": {
            "_id": {"circuit": "$weekends.circuit"},
            "wins_from_pole": {
                "$sum": {
                    "$cond": { "if": { "$eq": ["$weekends.race.results.grid", 1] }, "then": 1, "else": 0 }
                }
            },
            "number_of_races": {"$sum": 1}
        }
    },
    { "$match": { "number_of_races": {"$gte": 5} } },
    {
        "$addFields": {
            "wins_percentage": { "$divide": ["$wins_from_pole", "$number_of_races"] }
        }
    },
    { "$sort": {"wins_percentage": -1} },
    { "$limit": 10 },
    {
        "$project": {
            "_id": 0,
            "Circuit": "$_id.circuit.location.city",
            "Wins From Pole": "$wins_from_poles",
            "Races Count": "$number_of_races",
            "Win Percentage": "$wins_percentage"
        }
    }
])
query = collection.aggregate([
    { "$unwind": { "path": "$weekends" } },
    { "$match": { "weekends.race.pit_stops": { "$exists": True } } },
    { "$unwind": { "path": "$weekends.race.pit_stops" } },
    {
        "$group": {
            "_id": {
                "year": "$year",
                "circuit": "$weekends.circuit"
            },
            "avg_time": { "$avg": "$weekends.race.pit_stops.duration" }
        }
    },
    { "$match": {"_id.circuit.location.city": "Monza"} },
    {
        "$project": {
            "_id": 0,
            "Year": "$_id.year",
            "Average Time": "$avg_time"
        }
    },
    { "$sort": {"Year": 1} }
])
query = collection.aggregate([
    { "$unwind": {"path": "$weekends"} },
    { "$match": {"weekends.circuit.location.city": "Silverstone"} },
    {
        "$project": {
            "year": 1,
            "weekends.qualifying": 1
        }
    },
    { "$unwind": {"path": "$weekends.qualifying.results"} },
    { "$sort": {"weekends.qualifying.results.times.q1": 1} },
    { "$match": {"weekends.qualifying.results.times.q1": {"$exists": True}} },
    {
        "$group": {
            "_id": {"year": "$year"},
            "fastest_time": {"$first": "$weekends.qualifying.results.times.q1"}
        }
    },
    { "$sort": {"_id.year": 1} },
    {
        "$project": {
            "_id": 0,
            "Year": "$_id.year",
            "Fastest Time": "$fastest_time"
        }
    }
])
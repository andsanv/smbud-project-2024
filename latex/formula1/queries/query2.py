drivers = collection.aggregate([
    { "$unwind": {"path": "$weekends"} },
    { "$unwind": {"path": "$weekends.race.results"} },
    {
        "$group": {
            "_id": {"driver": "$weekends.race.results.car.driver"}
        }
    },
    {
        "$group": {
            "_id": {"nationality": "$_id.driver.nationality"},
            "count": {"$sum": 1}
        }
    },
    { "$sort": {"count": -1} },
    { "$limit": 10 },
    {
        "$project": {
            "_id": 0,
            "Country": "$_id.nationality",
            "Drivers Count": "$count",
        }
    }
])

constructors = collection.aggregate([
    { "$unwind": {"path": "$weekends"} },
    { "$unwind": {"path": "$weekends.race.results"} },
    {
        "$group": {
            "_id": {"constructor": "$weekends.race.results.car.constructor"}
        }
    },
    {
        "$group": {
            "_id": {"nationality": "$_id.constructor.nationality"},
            "count": {"$sum": 1}
        }
    },
    { "$sort": {"count": -1} },
    { "$limit": 10 },
    {
        "$project": {
            "_id": 0,
            "Country": "$_id.nationality",
            "Constructors Count": "$count",
        }
    }
])
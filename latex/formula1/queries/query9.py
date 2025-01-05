query = collection.aggregate([
    { "$unwind": { "path": "$weekends" } },
    { "$sort": { "weekends.round": -1 } },
    {
        "$group": {
            "_id": {"year": "$year"},
            "year": {"$first": "$year"},
            "weekend": {"$first": "$weekends"}
        }
    },
    {
        "$project": {
            "_id": 0,
            "year": 1,
            "weekend": 1
        }
    },
    { "$match": { "year": { "$gt": 1975 } } },
    { "$unwind": { "path": "$weekend.standings.drivers" } },
    { "$sort": { "weekend.standings.drivers.position": 1 } },
    {
        "$group": {
            "_id": {"year": "$year"},
            "year": {"$first": "$year"},
            "weekend": {"$first": "$weekend"}
        }
    },
    { "$unwind": { "path": "$weekend.standings.constructors" } },
    { "$sort": { "weekend.standings.constructors.position": 1 } },
    {
        "$group": {
            "_id": {"year": "$year"},
            "year": {"$first": "$year"},
            "weekend": {"$first": "$weekend"}
        }
    },
    {
        "$project": {
            "_id": 0,
            "year": 1,
            "weekend.race": 1,
            "weekend.standings": 1
        }
    },
    { "$unwind": { "path": "$weekend.race.results" } },
    {
        "$match": {
            "$and": [
                { "$expr": { "$eq": ["$weekend.race.results.car.driver.surname", "$weekend.standings.drivers.driver.surname"] } },
            ]
        }
    },
    {
        "$project": {
            "_id": 0,
            "year": 1,
            "weekend.race.results": 1,
            "weekend.standings": 1
        }
    },
    {
        "$match": {
            "$and": [
                { "$expr": { "$eq": ["$weekend.race.results.car.constructor.name", "$weekend.standings.constructors.constructor.name"] } },
            ]
        }
    },
    # {
    #     "$project": {
    #         "Year": "$year",
    #         "Name": "$weekend.race.results.car.driver.name",
    #         "Surname": "$weekend.race.results.car.driver.surname",
    #         "Constructor": "$weekend.race.results.car.constructor.name"
    #     }
    # },
    # { "$sort": {"Year": -1} },
    # { "$limit": 10 },
    { "$count": "Both Championships Winners" }
])
query = collection.aggregate([
    { "$unwind": { "path": "$weekends" } },
    { "$sort": { "weekends.round": -1 } },
    { 
        "$group": { 
            "_id": {"year": "$year"},
            "weekend": { "$first": "$weekends" }
        },
    },
    { 
        "$project": { 
            "year": "$_id.year",
            "weekends": "$weekend"
        }
    },
    { "$unwind": {"path": "$weekends.standings.constructors"} },
    {
        "$match": {
            "weekends.standings.constructors.constructor.name": {
                "$in": ["Ferrari", "Mercedes", "Red Bull", "McLaren", "Williams", "Renault", "Team Lotus", "Brabham", "Cooper"]
            }
        }
    },
    {
        "$project": {
            "constructor": "$weekends.standings.constructors.constructor.name",
            "year": "$_id.year",
            "position": "$weekends.standings.constructors.position"
        }
    },
    {
        "$sort": {
            "constructor": 1,
            "year": 1
        }
    },
    {
        "$project": {
            "_id": 0,
            "Year": "$_id.year",
            "Constructor": "$constructor",
            "Position": "$position"
        }
    }
])
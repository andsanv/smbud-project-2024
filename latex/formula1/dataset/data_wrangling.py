import csv
import json

input_folder: str = "csv/"
null_str: str = "\\N"



# HELPERS

def time_to_milliseconds(time: str) -> int:
    """
    Parses time expressed as "minutes:seconds.milliseconds" to just milliseconds.
    """
    if time == null_str:
        return time

    minutes_seconds, milliseconds = time.split(".")

    if ":" in minutes_seconds:
        minutes, seconds = minutes_seconds.split(":")
        return (int(minutes) * 60 + int(seconds)) * 10**3 + int(milliseconds)
    
    return int(seconds := minutes_seconds) * 10**3 + int(milliseconds)



# LOADERS

# general

def load_statuses() -> dict:
    """
    Reads status.csv and inserts data into a dictionary.
    """
    statuses = {}
    next(reader := csv.reader(open(input_folder + "status.csv")))

    for row in reader:
        status_id: int = int(row[0])
        statuses[status_id] = row[1]

    return statuses

def load_circuits() -> dict:
    """
    Reads circuits.csv and inserts data into a dictionary.
    """
    circuits = {}
    next(reader := csv.reader(open(input_folder + "circuits.csv")))

    for row in reader:
        circuit_id: int = int(row[0])

        circuit: dict = {
            "name": row[2],
            "location": {
                "city": row[3],
                "country": row[4]
            },
            "coordinates": {
                "latitude": float(row[5]),
                "longitude": float(row[6]),
                "altitude": int(row[7])
            }
        }

        circuits[circuit_id] = circuit

    return circuits

def load_drivers() -> dict:
    """
    Reads drivers.csv and inserts data into a dictionary.
    """
    drivers = {}
    next(reader := csv.reader(open(input_folder + "drivers.csv")))

    for row in reader:
        driver_id: int = int(row[0])

        driver: dict = {}

        if row[3] != null_str:
            driver["code"] = row[3]
        driver["name"] = row[4]
        driver["surname"] = row[5]
        driver["date_of_birth"] = row[6]
        driver["nationality"] = row[7]

        drivers[driver_id] = driver

    return drivers

def load_constructors() -> dict:
    """
    Reads constructors.csv and inserts data into a dictionary.
    """
    constructors = {}
    next(reader := csv.reader(open(input_folder + "constructors.csv")))

    for row in reader:
        constructor_id: int = int(row[0])

        constructor: dict = {
            "name": row[2],
            "nationality": row[3]
        }

        constructors[constructor_id] = constructor

    return constructors


# racing

def load_races_results(statuses: dict, drivers: dict, constructors: dict) -> dict:
    """
    Reads races.csv and inserts data into a dictionary.
    """
    results = {}
    next(reader := csv.reader(open(input_folder + "results.csv")))

    for row in reader:
        id: int = int(row[1])
        result: dict = {}

        result["grid"] = int(row[5]) # starting grid position
        if row[6] != null_str:  # finishing position
            result["position"] = int(row[6])
        result["order"] = int(row[8]) # order of finishing, does not count for retirements
        result["car"] = {  # car containing driver and constructor
            "number": int(row[4]),
            "driver": drivers[int(row[2])],
            "constructor": constructors[int(row[3])]
        }
        result["points"] = float(row[9])
        result["laps"] = int(row[10])
        if row[12] != null_str:
            result["time"] = int(row[12])
        if not (row[13] == row[15] == null_str and (row[14] == "0" or row[14] == null_str)):
            result["fastest_lap"] = {
                "lap": int(row[13]),
                "rank": int(row[14]),
                "time": time_to_milliseconds(row[15])
            }
        result["status"] = statuses[int(row[17])]

        if id not in results:
            results[id] = [result]
        else:
            results[id].append(result)

    return results

def load_pit_stops(drivers: dict) -> dict:
    """
    Reads pit_stops.csv and inserts data into a dictionary.
    """
    pit_stops = {}
    next(reader := csv.reader(open(input_folder + "pit_stops.csv")))

    for row in reader:
        id: int = int(row[0])

        pit_stop: dict = {
            "driver": drivers[int(row[1])],
            "stop": int(row[2]),
            "lap": int(row[3]),
            "time": row[4],
            "duration": int(row[6])
        }

        if id in pit_stops:
            pit_stops[id].append(pit_stop)
        else:
            pit_stops[id] = [pit_stop]

    return pit_stops

def load_races(statuses: dict, drivers: dict, constructors: dict) -> dict:
    """
    Reads race related files and returns a dictionary.
    """
    races: dict = {}

    results: dict = load_races_results(statuses, drivers, constructors)
    pit_stops: dict = load_pit_stops(drivers)

    for id, res in results.items():
        races[id] = { "results": res }

    for id, pit in pit_stops.items():
        races[id]["pit_stops"] = pit

    return races

def load_qualifyings(drivers: dict, constructors: dict) -> dict:
    """
    Reads qualifying.csv and inserts data into a dictionary.
    """
    qualifyings = {}
    next(reader := csv.reader(open(input_folder + "qualifying.csv")))

    for row in reader:
        id: int = int(row[1])
        qualifying_result = {}

        qualifying_result["position"] = int(row[5])
        qualifying_result["car"] = {
            "number": int(row[4]),
            "driver": drivers[int(row[2])],
            "constructor": constructors[int(row[3])]
        }
        if not (row[6] == null_str and row[7] == null_str and row[8] == null_str):
            qualifying_result["times"] = {}
            if row[6] != null_str:
                qualifying_result["times"]["q1"] = time_to_milliseconds(row[6])
            if row[7] != null_str:
                qualifying_result["times"]["q2"] = time_to_milliseconds(row[7])
            if row[8] != null_str:
                qualifying_result["times"]["q3"] = time_to_milliseconds(row[8])

        if id not in qualifyings:
            qualifyings[id] = { "results": [qualifying_result] }
        else:
            qualifyings[id]["results"].append(qualifying_result)

    return qualifyings

def load_sprints(statuses: dict, drivers: dict, constructors: dict) -> dict:
    """
    Reads sprint_results.csv and inserts data into a dictionary.
    """
    sprints = {}
    next(reader := csv.reader(open(input_folder + "sprint_results.csv")))

    for row in reader:
        id: int = int(row[1])
        sprint_result: dict = {}

        sprint_result["grid"] = int(row[5]) # starting grid position
        if row[6] != null_str:  # finishing position
            sprint_result["position"] = int(row[6])
        sprint_result["order"] = int(row[8]) # order of finishing, does not count for retirements
        sprint_result["car"] = {  # car containing driver and constructor
            "number": int(row[4]),
            "driver": drivers[int(row[2])],
            "constructor": constructors[int(row[3])]
        }
        sprint_result["points"] = float(row[9])
        sprint_result["laps"] = int(row[10])
        if row[12] != null_str:
            sprint_result["time"] = int(row[12])
        if not (row[13] == null_str and row[14] == null_str):
            sprint_result["fastest_lap"] = {
                "lap": int(row[13]),
                "time": time_to_milliseconds(row[14])
            }
        sprint_result["status"] = statuses[int(row[15])]

        if id not in sprints:
            sprints[id] = { "results": [sprint_result] }
        else:
            sprints[id]["results"].append(sprint_result)

    return sprints


# standings

def load_drivers_standings(drivers: dict) -> dict:
    """
    Reads driver_standings.csv and inserts data into a dictionary.
    """
    standings = {}
    next(reader := csv.reader(open(input_folder + "driver_standings.csv")))

    for row in reader:
        id: int = int(row[1])   # weekend id

        standing: dict = {
            "position": int(row[4]),
            "driver": drivers[int(row[2])],
            "points": float(row[3]),
            "wins": int(row[6])
        }

        if id in standings:
            standings[id].append(standing)
        else:
            standings[id] = [standing]

    return standings

def load_constructors_standings(constructors: dict) -> dict:
    """
    Reads constructors_standings.csv and inserts data into a dictionary.
    """
    standings = {}
    next(reader := csv.reader(open(input_folder + "constructor_standings.csv")))

    for row in reader:
        id: int = int(row[1])   # weekend id

        standing: dict = {
            "position": int(row[4]),
            "constructor": constructors[int(row[2])],
            "points": float(row[3]),
            "wins": int(row[6])
        }

        if id in standings:
            standings[id].append(standing)
        else:
            standings[id] = [standing]

    return standings

def load_standings(drivers: dict, constructors: dict) -> dict:
    """
    Reads standings related files and returns a dictionary.
    """
    drivers_standings: dict = load_drivers_standings(drivers)
    constructors_standings: dict = load_constructors_standings(constructors)

    standings: dict = {}

    for id, drv in drivers_standings.items():
        standings[id] = { "drivers": drv }

    for id, cst in constructors_standings.items():
        standings[id]["constructors"] = cst

    return standings


def load_weekends(circuits: dict, qualifyings: dict, races: dict, sprints: dict, standings: dict) -> dict:
    """
    Reads races.csv and builds a single structure that unifies all others.
    """
    weekends = {}
    next(reader := csv.reader(open(input_folder + "races.csv")))

    for row in reader:
        id: int = int(row[0])
        year: int = int(row[1])

        weekend: dict = {
            "round": int(row[2]),
            "circuit": circuits[int(row[3])],
            "date": row[5]
        }

        if id in qualifyings:
            weekend["qualifying"] = qualifyings[id]
        if id in races:
            weekend["race"] = races[id]
        if id in sprints:
            weekend["sprint"] = sprints[id]
        if id in standings:
            weekend["standings"] = standings[id]

        if year not in weekends:
            weekends[year] = [weekend]
        else:
            weekends[year].append(weekend)
    
    return weekends

def build_championships() -> dict:
    """
    Returns a dictionary file containing all data.
    """
    statuses: dict = load_statuses()
    circuits: dict = load_circuits()
    drivers: dict = load_drivers()
    constructors: dict = load_constructors()

    races: dict = load_races(statuses, drivers, constructors)
    qualifyings: dict = load_qualifyings(drivers, constructors)
    sprints: dict = load_sprints(statuses, drivers, constructors)

    standings: dict = load_standings(drivers, constructors)

    weekends: dict = load_weekends(circuits, qualifyings, races, sprints, standings)

    championships: list = []
    for year, ws in weekends.items():
        championships.append({
            "year": year,
            "weekends": ws
        })

    return sorted(championships, key=(lambda x : x["year"]))
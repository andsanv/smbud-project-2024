import csv
import json

input_folder: str = "csv/"
null_str: str = "\\N"

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
            "constructor": constructors[int(row[3])],
        }
        if not (
            row[6] == null_str and
            row[7] == null_str and
            row[8] == null_str
        ):
            qualifying_result["times"] = {}
            if row[6] != null_str:
                qualifying_result["times"]["q1"] = time_to_ms(row[6])
            if row[7] != null_str:
                qualifying_result["times"]["q2"] = time_to_ms(row[7])
            if row[8] != null_str:
                qualifying_result["times"]["q3"] = time_to_ms(row[8])

        if id not in qualifyings:
            qualifyings[id] = {"results": [qualifying_result]}
        else:
            qualifyings[id]["results"].append(qualifying_result)

    return qualifyings


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
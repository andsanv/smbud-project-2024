import json
from data_wrangling import build_championships

def main():
    """
    Dumps the dataset in a local folder.
    """
    json.dump(build_championships(), open("json/dataset.json", 'w'))

main()
import json
from data_wrangling import build_championships

def main():
    """
    Dumps the dataset in a local folder.
    """
    json.dump(build_championships(), open("dump.json", 'w'))

main()
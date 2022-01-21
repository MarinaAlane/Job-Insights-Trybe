import csv
import pprint
from functools import lru_cache

pp = pprint.PrettyPrinter(indent=4)


@lru_cache
def read(path):
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",", quotechar='"')
        return [row for row in reader]

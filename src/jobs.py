from functools import lru_cache
import csv
# hello


@lru_cache
def read(path):
  with open(path) as file:
  get_jobs = csv.DictReader(file, delimiter=",", quotechar='"')
  content = list(get_jobs)
return content

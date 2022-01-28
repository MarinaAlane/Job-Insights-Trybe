import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs_list = []
        for row in jobs_reader:
            new_job = {}
            new_job["job_title"] = row["job_title"]
            new_job["company"] = row["company"]
            new_job["state"] = row["state"]
            new_job["city"] = row["city"]
            new_job["min_salary"] = row["min_salary"]
            new_job["max_salary"] = row["max_salary"]
            new_job["job_desc"] = row["job_desc"]
            new_job["industry"] = row["industry"]
            new_job["rating"] = row["rating"]
            new_job["date_posted"] = row["date_posted"]
            new_job["valid_until"] = row["valid_until"]
            new_job["job_type"] = row["job_type"]
            new_job["id"] = row["id"]
            jobs_list.append(new_job)
        return jobs_list

# new_title["job_title"] = row["job_title"]
# company,state,city,min_salary,max_salary,job_desc,industry,rating,date_posted,valid_until,job_type,id
# new_job = {}
# new_job["job_title"] = row["job_title"]
# new_job["company"] = row["company"]
# new_job["state"] = row["state"]
# new_job[]

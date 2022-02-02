from src.jobs import read
from src.insights import (
    get_unique_job_types,
    get_unique_industries,
    get_max_salary,
    get_min_salary,
    filter_by_job_type,
    matches_salary_range,
    filter_by_salary_range,
)

csv_file = "./src/jobs.csv"
job = {"min_salary": 200, "max_salary": 10000}
job_types = [
    {"id": 1, "job_type": "PART_TIME"},
    {"id": 2, "job_type": "PART_TIME"},
    {"id": 3, "job_type": "OTHER"},
    {"id": 4, "job_type": "OTHER"},
    {"id": 5, "job_type": "FULL_TIME"},
    {"id": 6, "job_type": "FULL_TIME"},
    {"id": 7, "job_type": "CONTRACTOR"},
    {"id": 8, "job_type": "CONTRACTOR"},
    {"id": 9, "job_type": "TEMPORARY"},
    {"id": 10, "job_type": "TEMPORARY"},
    {"id": 11, "job_type": "INTERN"},
    {"id": 12, "job_type": "INTERN"},
]
jobs = [
    {"max_salary": 0, "min_salary": 10},
    {"max_salary": 10, "min_salary": 100},
    {"max_salary": 10000, "min_salary": 200},
    {"max_salary": 15000, "min_salary": 0},
    {"max_salary": 1500, "min_salary": 0},
    {"max_salary": -1, "min_salary": 10},
]

read(csv_file)
get_unique_job_types(csv_file)
get_unique_industries(csv_file)
get_max_salary(csv_file)
get_min_salary(csv_file)
filter_by_job_type(job_types, "FULL_TIME")
print(matches_salary_range(job, '200'))
filter_by_salary_range(jobs, 1000)

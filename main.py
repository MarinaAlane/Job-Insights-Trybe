from src.jobs import read
from src.insights import (
    get_unique_job_types,
    get_unique_industries,
    get_max_salary,
    get_min_salary,
    filter_by_job_type,
    filter_by_industry,
    matches_salary_range,
    filter_by_salary_range
)
from src.sorting import sort_by

read("src/jobs.csv")

get_unique_job_types("src/jobs.csv")

get_unique_industries("src/jobs.csv")

get_max_salary("src/jobs.csv")

get_min_salary("src/jobs.csv")

filter_by_job_type(read("src/jobs.csv"), "CONTRACTOR")

filter_by_industry(read("src/jobs.csv"), "Manufacturing")

salarys = {"max_salary": 10, "min_salary": 0}

matches_salary_range(salarys, 1000)

filter_by_salary_range(read("src/jobs.csv"), 1000)

print(sort_by(read("src/jobs.csv"), 'max_salary'))

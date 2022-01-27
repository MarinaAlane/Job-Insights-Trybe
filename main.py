from src.jobs import read
from src.insights import (
    get_unique_job_types,
    get_unique_industries,
    get_max_salary
)

read("src/jobs.csv")

get_unique_job_types("src/jobs.csv")

get_unique_industries("src/jobs.csv")

get_max_salary("src/jobs.csv")

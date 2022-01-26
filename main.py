from src.jobs import read
from src.insights import get_unique_job_types

read("src/jobs.csv")

get_unique_job_types("src/jobs.csv")

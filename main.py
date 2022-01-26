from src.jobs import read
from src.insights import get_unique_job_types, get_unique_industries

read("src/jobs.csv")

get_unique_job_types("src/jobs.csv")

get_unique_industries("src/jobs.csv")

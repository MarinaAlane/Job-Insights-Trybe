from src.jobs import read
from src.insights import get_unique_job_types, get_unique_industries

csv_file = './src/jobs.csv'

read(csv_file)
get_unique_job_types(csv_file)
get_unique_industries(csv_file)

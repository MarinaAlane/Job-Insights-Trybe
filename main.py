from src.jobs import read
from src.insights import (
    get_unique_job_types,
    get_unique_industries,
    get_max_salary,
    get_min_salary,
    # filter_by_job_type,
)

csv_file = "./src/jobs.csv"


read(csv_file)
get_unique_job_types(csv_file)
get_unique_industries(csv_file)
get_max_salary(csv_file)
get_min_salary("tests/mocks/jobs_with_salaries.csv")
# filter_by_job_type(read(csv_file), "full time")

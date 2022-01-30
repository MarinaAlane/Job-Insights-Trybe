from src.jobs import read


def get_unique_job_types(path):
    data_jobs = read(path)
    types = set()
    for job in data_jobs:
        types.add(job["job_type"])
    return types


def filter_by_job_type(jobs, job_type):
    types = []
    for job in jobs:
        if job["job_type"] == job_type:
            types.append(job)
    return types


def get_unique_industries(path):
    data_jobs = read(path)
    industries = set()
    for job in data_jobs:
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    types = []
    for job in jobs:
        if job["industry"] == industry:
            types.append(job)
    return types


def get_max_salary(path):
    jobs = read(path)
    salaries = set()
    for job in jobs:
        if job["max_salary"] != "" and job["max_salary"].isnumeric():
            salaries.add(int(job["max_salary"]))
    return max(salaries)


def get_min_salary(path):
    jobs = read(path)
    salaries = set()
    for job in jobs:
        if job["min_salary"] != "" and job["min_salary"].isnumeric():
            salaries.add(int(job["min_salary"]))
    return min(salaries)


def matches_salary_range(job, salary):
    print(job)
    print(salary)
    if (
        "max_salary" not in job
        or "min_salary" not in job
        or not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or not isinstance(salary, int)
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError("Error")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):

    return []

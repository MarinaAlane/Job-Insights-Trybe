from .jobs import read
from .Utils.salary_range_validations import salary_range_validation


def get_unique_job_types(path):
    jobs = read(path)

    job_types = set()
# https://www.geeksforgeeks.org/set-add-python/
# https://www.geeksforgeeks.org/python-convert-set-into-a-list/
    for job in jobs:
        job_types.add(job["job_type"])
    return list(job_types)


def filter_by_job_type(jobs, job_type):

    filtered_jobs = [
        job for job in jobs if job["job_type"] == job_type
    ]
    return filtered_jobs


def get_unique_industries(path):
    jobs = read(path)
    industries = set()
    for job in jobs:
        if job["industry"] != "":
            industries.add(job["industry"])
    return list(industries)


def filter_by_industry(jobs, industry):
    filtered_jobs = [
        job for job in jobs if job["industry"] == industry
    ]
    return filtered_jobs


def get_max_salary(path):
    jobs = read(path)

    max_salary = 0
    for job in jobs:
        if job["max_salary"].isnumeric():
            if int(job["max_salary"]) > max_salary:
                max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path):
    jobs = read(path)

    min_salary = get_max_salary(path)
    for job in jobs:
        if job["min_salary"].isnumeric():
            if int(job["min_salary"]) < min_salary:
                min_salary = int(job["min_salary"])
    return min_salary


def matches_salary_range(job, salary):
    salary_range_validation(job, salary)
    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range
    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []

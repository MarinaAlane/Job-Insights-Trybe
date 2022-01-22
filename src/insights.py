# https://www.w3schools.com/python/python_sets.asp
# https://stackoverflow.com/questions/10406130/check-if-something-is-not-in-a-list-in-python/10406143
# https://pt.stackoverflow.com/questions/127118/python-diferen%C3%A7a-entre-assert-e-raise
from src.jobs import read


def get_unique_job_types(path):
    try:
        data = read(path)
        types_jobs = set()
        for job in data:
            types_jobs.add(job["job_type"])
        return types_jobs
    except FileNotFoundError:
        print("file not found or corrupted")


def filter_by_job_type(jobs, job_type):
    selected_jobs = []
    for job in jobs:
        if (job["job_type"] == job_type):
            try:
                selected_jobs.append(job)
            except ValueError:
                continue
    return selected_jobs


def get_unique_industries(path):
    try:
        data = read(path)
        industries = set()
        for job in data:
            if (job["industry"] != ""):
                industries.add(job["industry"])
        return industries
    except FileNotFoundError:
        print("file not found or corrupted")


def filter_by_industry(jobs, industry):
    selected_industries = []
    for job in jobs:
        if (job["industry"] == industry):
            try:
                selected_industries.append(job)
            except ValueError:
                continue
    return selected_industries


def get_max_salary(path):
    data = read(path)
    salaries = []
    for job in data:
        if (job["max_salary"] != ""):
            try:
                salary = int(float(job["max_salary"]))
                salaries.append(salary)
            except ValueError:
                continue
    return max(salaries)


def get_min_salary(path):
    data = read(path)
    salaries = []
    for job in data:
        if (job["min_salary"] != ""):
            try:
                salary = int(float(job["min_salary"]))
                salaries.append(salary)
            except ValueError:
                continue
    return min(salaries)


def matches_salary_range(job, salary):
    if ("max_salary" not in job or "min_salary" not in job):
        raise ValueError
    elif (
        not type(job["min_salary"]) is int or
        not type(job["max_salary"]) is int or
        not type(salary) is int
    ):
        raise ValueError
    elif (job["min_salary"] >= job["max_salary"]):
        raise ValueError
    elif (job["min_salary"] <= salary <= job["max_salary"]):
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    filters_jobs = []
    for job in jobs:
        try:
            if (matches_salary_range(job, salary)):
                filters_jobs.append(job)
        except ValueError:
            continue
    return filters_jobs

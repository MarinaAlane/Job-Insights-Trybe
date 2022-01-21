from src.jobs import read
from src.helpers.salary_helpers import get_salary_list
from src.helpers.job_helpers import is_valid_job


def get_unique_job_types(path):
    jobs = read(path)
    unique_jobs = set()
    for job in jobs:
        unique_jobs.add(job["job_type"])
    return unique_jobs


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    jobs = read(path)
    unique_industries = set()
    for job in jobs:
        industry = job["industry"].strip()
        if not industry == "":
            unique_industries.add(industry)
    return unique_industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    jobs = read(path)
    salaries = get_salary_list(jobs, "max_salary")
    return max(salaries)


def get_min_salary(path):
    jobs = read(path)
    salaries = get_salary_list(jobs, "min_salary")
    return min(salaries)


def matches_salary_range(job, salary):
    try:
        min_salary = job["min_salary"]
        max_salary = job["max_salary"]

        is_valid = is_valid_job(job, salary)

        if not is_valid:
            raise ValueError()

        return min_salary <= salary <= max_salary
    except KeyError:
        raise ValueError()


def filter_by_salary_range(jobs, salary):
    if not type(salary) is int:
        return []

    valid_jobs = [job for job in jobs if is_valid_job(job)]

    jobs_in_salary_range = [
        job for job in valid_jobs if matches_salary_range(job, salary)
    ]

    return jobs_in_salary_range

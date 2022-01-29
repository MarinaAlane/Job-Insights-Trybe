from src.jobs import read


def get_unique_job_types(path):
    jobs_reader = read(path)
    job_types = []
    for job in jobs_reader:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    filtered = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered.append(job)
    return filtered


def get_unique_industries(path):
    jobs_reader = read(path)
    industries = []
    for job in jobs_reader:
        if job["industry"] not in industries and job["industry"] != "":
            industries.append(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    filtered = []
    for job in jobs:
        if job["industry"] == industry:
            filtered.append(job)
    return filtered


def get_max_salary(path):
    jobs_reader = read(path)
    max_salary = 0
    for job in jobs_reader:
        try:
            if int(float(job["max_salary"])) > max_salary:
                max_salary = int(float(job["max_salary"]))
        except ValueError:
            continue
    return max_salary


def get_min_salary(path):
    jobs_reader = read(path)
    min_salary = 0
    for job in jobs_reader:
        try:
            if int(float(job["min_salary"])) < min_salary or min_salary == 0:
                min_salary = int(float(job["min_salary"]))
        except ValueError:
            continue
    return min_salary


def matches_salary_range(job, salary):
    if (
        "max_salary" not in job or
        "min_salary" not in job or
        type(job["max_salary"]) != int or
        type(job["min_salary"]) != int or
        type(salary) != int or
        job["max_salary"] < job["min_salary"]
    ):
        raise ValueError
    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    filtered = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered.append(job)
        except ValueError:
            continue
    return filtered

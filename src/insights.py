from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_types = []
    for job in jobs:
        if job["job_type"] not in job_types and job["job_type"]:
            job_types.append(job['job_type'])
        else:
            job_types
    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    jobs = read(path)
    industrys = []
    for job in jobs:
        if job["industry"] not in industrys and job["industry"]:
            industrys.append(job['industry'])
        else:
            industrys
    return industrys


def filter_by_industry(jobs, industry):
    filtered_industrys = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_industrys.append(job)
    return filtered_industrys


def get_max_salary(path):
    jobs = read(path)
    max_salary = 0
    for job in jobs:
        if job["max_salary"] and job["max_salary"] != 'invalid':
            if max_salary < int(job["max_salary"]):
                max_salary = int(job["max_salary"])
            else:
                max_salary
    return max_salary


def get_min_salary(path):
    jobs = read(path)
    min_salary = 0
    for job in jobs:
        if job["min_salary"] and job["min_salary"] != 'invalid':
            if min_salary > int(job["min_salary"]) or min_salary == 0:
                min_salary = int(job["min_salary"])
            else:
                min_salary
    return min_salary


def matches_salary_range(job, salary):
    if not ("min_salary" in job and "max_salary" in job):
        raise ValueError("min_salary and max_salary must be provided")

    elif not (
        isinstance(job["min_salary"], int)
        and
        isinstance(job["max_salary"], int)
    ):
        raise ValueError("min_salary and max_salary must be integers")

    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary can't be greater than max_salary")

    elif not isinstance(salary, int):
        raise ValueError("salary must be an integer")

    else:
        return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filtered_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_salary.append(job)
        except ValueError:
            pass
    return filtered_salary

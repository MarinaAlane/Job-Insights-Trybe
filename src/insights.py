from src import jobs


def get_unique_job_types(path):
    jobs_data = jobs.read(path)
    unique_job_types = []
    for job in jobs_data:
        if job["job_type"] not in unique_job_types:
            unique_job_types.append(job["job_type"])
    return unique_job_types


def filter_by_job_type(jobs, job_type):
    job_types = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_types.append(job)
    return job_types


def get_unique_industries(path):
    jobs_data = jobs.read(path)
    unique_industries = set()
    for job in jobs_data:
        if job["industry"]:
            unique_industries.add(job["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    industries = []
    for job in jobs:
        if job["industry"] == industry:
            industries.append(job)
    return industries


def get_max_salary(path):
    jobs_data = jobs.read(path)
    max_salary = set()
    for job in jobs_data:
        try:
            if job["max_salary"]:
                max_salary.add(int(job["max_salary"]))
        except ValueError:
            pass
    return max(max_salary)


def get_min_salary(path):
    jobs_data = jobs.read(path)
    min_salary = set()
    for job in jobs_data:
        try:
            if job["min_salary"]:
                min_salary.add(int(job["min_salary"]))
        except ValueError:
            pass
    return min(min_salary)


def matches_salary_range(job, salary):
    if not ("max_salary" in job and "min_salary" in job):
        raise ValueError()
    elif (
        type(job["min_salary"]) != int or
        type(job["max_salary"]) != int or
        type(salary) != int
    ):
        raise ValueError()
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError()
    elif int(job["min_salary"] <= salary <= job["max_salary"]):
        return True
    return False


def filter_by_salary_range(jobs, salary):
    salary_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salary_range.append(job)
        except ValueError:
            pass
    return salary_range

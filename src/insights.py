from logging import exception
from src import jobs

# import jobs


def get_unique_job_types(path):
    jobs_list = jobs.read(path)
    job_types = list()
    for job in jobs_list:
        if job["job_type"] in job_types:
            pass
        else:
            job_types.append(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    jobs_by_job_type = list()
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_by_job_type.append(job)
        else:
            continue
    return jobs_by_job_type


def get_unique_industries(path):
    jobs_list = jobs.read(path)
    job_industries = list()
    for job in jobs_list:
        if job["industry"] == "" or job["industry"] in job_industries:
            pass
        else:
            job_industries.append(job["industry"])
    return job_industries


def filter_by_industry(jobs, industry):
    jobs_by_industry = list()
    for job in jobs:
        if job["industry"] == industry:
            jobs_by_industry.append(job)
        else:
            continue
    return jobs_by_industry


def get_max_salary(path):
    job_list = jobs.read(path)
    highest_salary = 0
    for job in job_list:
        if job["max_salary"] == "" or not job["max_salary"].isnumeric():
            continue
        elif int(job["max_salary"]) > highest_salary:
            highest_salary = int(job["max_salary"])
    return highest_salary


def get_min_salary(path):
    job_list = jobs.read(path)
    lowest_salary = 0
    for job in job_list:
        if job["min_salary"] == "" or not job["min_salary"].isnumeric():
            continue
        elif lowest_salary == 0 or int(job["min_salary"]) < lowest_salary:
            lowest_salary = int(job["min_salary"])
    return lowest_salary


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Entries doesn't exists")
    elif (
        not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or not isinstance(salary, int)
    ):
        raise ValueError("Invalid entries")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary is greater than max_salary")
    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    jobs_by_salary_range = list()

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_by_salary_range.append(job)
        except ValueError:
            pass
    return jobs_by_salary_range

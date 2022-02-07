from src.jobs import read

# import pprint


def get_unique_job_types(path):
    data_jobs = read(path)
    unique_job_types = list({job["job_type"] for job in data_jobs})
    return unique_job_types


def filter_by_job_type(jobs, job_type):
    filtered_job_type = [job for job in jobs if job["job_type"] == job_type]
    return filtered_job_type


def get_unique_industries(path):
    data_jobs = read(path)
    unique_industries = list(
        {job["industry"] for job in data_jobs if len(job["industry"]) > 0}
    )
    return unique_industries


def filter_by_industry(jobs, industry):
    filtered_industry = [job for job in jobs if job["industry"] == industry]
    return filtered_industry


def get_max_salary(path):
    data_jobs = read(path)
    max_salary = max(
        [
            int(job["max_salary"])
            for job in data_jobs
            if job["max_salary"].isnumeric() is True
        ]
    )
    return max_salary


def get_min_salary(path):
    data_jobs = read(path)
    min_salary = min(
        [
            int(job["min_salary"])
            for job in data_jobs
            if job["min_salary"].isnumeric() is True
        ]
    )
    return min_salary


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError()
    if (
        type(job["min_salary"]) is not int or
        type(job["max_salary"]) is not int or
        type(salary) is not int
    ):
        raise ValueError()
    if (job["min_salary"] > job["max_salary"]):
        raise ValueError()
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


# https://learncodeimprove.com/python/list-of-unique-items-comprehension/
# https://www.w3schools.com/python/ref_string_isnumeric.asp

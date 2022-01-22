from src import jobs
import math


def get_unique_job_types(path):
    jobs_list = jobs.read(path)
    job_types = []
    for job in jobs_list:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return list(set(job_types))


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    job_list = jobs.read(path)
    job_industries = []
    for job in job_list:
        if job["industry"] not in job_industries and job["industry"]:
            job_industries.append(job["industry"])
    return list(set(job_industries))


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    job_list = jobs.read(path)
    max_salary = 0
    for job in job_list:
        try:
            if int(job["max_salary"]) > max_salary:
                max_salary = int(job["max_salary"])
        except ValueError:
            pass
    return max_salary


def get_min_salary(path):
    jobs_list = jobs.read(path)
    min_salary = math.inf
    for job in jobs_list:
        try:
            if int(job["min_salary"]) < min_salary:
                min_salary = int(job["min_salary"])
        except ValueError:
            pass
    return min_salary


def matches_salary_range(job, salary):
    pass


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

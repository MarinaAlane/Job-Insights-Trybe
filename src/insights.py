from src.jobs import read


def get_unique_job_types(path):
    jobs_data = read(path)
    job_types = set()

    for job in jobs_data:
        job_types.add(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = [job for job in jobs if job["job_type"] == job_type]

    return filtered_jobs


def get_unique_industries(path):
    jobs_data = read(path)
    job_industry = set()

    for job in jobs_data:
        if job["industry"]:
            job_industry.add(job["industry"])

    return job_industry


def filter_by_industry(jobs, industry):
    filtered_jobs = [job for job in jobs if job["industry"] == industry]

    return filtered_jobs


def get_max_salary(path):
    jobs_data = read(path)
    job_salaries = set()

    for job in jobs_data:
        if job["max_salary"].isnumeric():
            job_salaries.add(int(job["max_salary"]))
    return max(job_salaries)


def get_min_salary(path):
    jobs_data = read(path)
    job_salaries = set()

    for job in jobs_data:
        if job["min_salary"].isnumeric():
            job_salaries.add(int(job["min_salary"]))
    return min(job_salaries)


# Ref: https://www.w3schools.com/python/python_operators.asp (not in, is not)
# https://www.w3schools.com/python/python_try_except.asp (raise)
def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError()

    if (
        type(job["min_salary"]) is not int or
        type(job["max_salary"]) is not int or
        type(salary) is not int
    ):
        raise ValueError()

    if job["min_salary"] > job["max_salary"]:
        raise ValueError()

    return job["min_salary"] <= salary <= job["max_salary"]


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

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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
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

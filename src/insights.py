from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)

    job_types = set(job["job_type"] for job in jobs)

    return job_types


def filter_by_job_type(jobs, job_type):
    filter_job = list()

    for job in jobs:
        if job["job_type"] == job_type:
            filter_job.append(job)

    return filter_job


def get_unique_industries(path):
    jobs = read(path)

    industries = set()

    for industry in jobs:
        if industry["industry"] != "":
            industries.add(industry["industry"])

    return industries


def filter_by_industry(jobs, industry):
    filter_job = list()

    for job in jobs:
        if job["industry"] == industry:
            filter_job.append(job)

    return filter_job


def get_max_salary(path):
    jobs = read(path)

    salaries = list()
    # http://www.w3big.com/pt/python/att-string-isnumeric.html
    for salary in jobs:
        if salary["max_salary"].isnumeric():
            salaries.append(int(salary["max_salary"]))

    return max(salaries)


def get_min_salary(path):
    jobs = read(path)

    salaries = set()

    for salary in jobs:
        if salary["min_salary"].isnumeric():
            salaries.add(int(salary["min_salary"]))

    return min(salaries)


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

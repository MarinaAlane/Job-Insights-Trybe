from src.jobs import read


def get_unique_job_types(path):
    arr = read(path)
    unique_arr = set()
    for job in arr:
        unique_arr.add(job["job_type"])

    return unique_arr


def filter_by_job_type(jobs, job_type):
    arr = []
    for job in jobs:
        if job["job_type"] == job_type:
            arr.append(job)
    
    return arr


def get_unique_industries(path):
    arr = read(path)
    industries_arr = set()
    for job in arr:
        if job['industry'] != '':
            industries_arr.add(job["industry"])

    return industries_arr


def filter_by_industry(jobs, industry):
    arr = []
    for job in jobs:
        if job["industry"] == industry:
            arr.append(job)
    
    return arr


def get_max_salary(path):
    arr = read(path)
    industries_arr = []
    for job in arr:
        if job['max_salary'] != '' and job['max_salary'].isnumeric():
            industries_arr.append(int(job['max_salary']))

    industries_arr.sort(reverse=True)
    return int(industries_arr[0])


def get_min_salary(path):
    arr = read(path)
    industries_arr = []
    for job in arr:
        if job['min_salary'] != '' and job['min_salary'].isnumeric():
            industries_arr.append(int(job['min_salary']))

    industries_arr.sort()
    return int(industries_arr[0])


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

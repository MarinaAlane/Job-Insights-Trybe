from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    list_of_jobs = read(path)
    result = []
    for job in list_of_jobs:
        if job['job_type'] not in result:
            result.append(job['job_type'])
    return result


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    result = []
    for job in jobs:
        if job['job_type'] == job_type:
            result.append(job)
    return result


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    list_of_jobs = read(path)
    result = []
    for job in list_of_jobs:
        if len(job['industry']) > 0:
            if job['industry'] not in result:
                result.append(job['industry'])
    return result


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    result = []
    for job in jobs:
        if job['industry'] == industry:
            result.append(job)
    return result


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    list_of_jobs = read(path)
    result = 0
    for job in list_of_jobs:
        if job['max_salary'].isnumeric():
            if int(job['max_salary']) > result:
                result = int(job['max_salary'])
    return result


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    list_of_jobs = read(path)
    result = float("inf")
    for job in list_of_jobs:
        if job['min_salary'].isnumeric():
            if int(job['min_salary']) < result:
                result = int(job['min_salary'])
    return result


def verify_salary(salary):
    if not isinstance(salary, int):
        raise ValueError('Salary is not a valid integer')


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
    min_salary = job.get("min_salary", None)
    max_salary = job.get("max_salary", None)
    if (min_salary is None or max_salary is None):
        raise ValueError('Salary is missing')
    if not (isinstance(min_salary, int) and isinstance(max_salary, int)):
        raise ValueError('Salary type is invalid')
    if (min_salary < 0 or max_salary < 0):
        raise ValueError('Salary is not numeric')
    if (min_salary > max_salary):
        raise ValueError('Min_salary is greater than max_salary')
    verify_salary(salary)
    return min_salary <= salary <= max_salary


# print(matches_salary_range({"max_salary": 10000, "min_salary": 0}, 300))


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

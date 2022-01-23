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
    arr_csv = read(path)
    types_jobs = set()
    for item in arr_csv:
        for job in item["job_type"].split(","):
            types_jobs.add(job)
    return types_jobs


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
    filter_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filter_jobs.append(job)
    return filter_jobs


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
    arr_csv = read(path)
    industries = set()
    for item in arr_csv:
        industry = item["industry"]
        if industry != "":
            industries.add(industry)
    return industries


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
    filter_industry = []
    for job in jobs:
        if job["industry"] == industry:
            filter_industry.append(job)
    return filter_industry


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

    arr_csv = read(path)
    max_salaries = []
    for item in arr_csv:
        if item["max_salary"] != "" and item["max_salary"] != "invalid":
            max_salaries.append(int(item["max_salary"]))
    max_salaries.sort()
    return max_salaries[-1]


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
    arr_csv = read(path)
    min_salaries = []
    for item in arr_csv:
        if item["min_salary"] != "" and item["min_salary"] != "invalid":
            min_salaries.append(int(item["min_salary"]))
    min_salaries.sort()
    return min_salaries[0]


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
    if not (job['min_salary'] and job['max_salary']):
        raise ValueError('min_salary and max_salary must be provided')
    elif not (int(job['max_salary']) and int(job['min_salary'])):
        raise ValueError('min_salary and max_salary must be integers')
    elif (job['max_salary'] > job['min_salary']):
        raise ValueError("min_salary can't be greater than max_salary")
    elif not (int(salary)):
        raise ValueError('salary must be an integer')
    else:
        return job['min_salary'] <= salary <= job['max_salary']


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

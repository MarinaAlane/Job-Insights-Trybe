from .jobs import read


def get_unique_job_types(path):
    data = read(path)
    jobs_types = set()
    for job_type in data:
        jobs_types.add(job_type['job_type'])
    return jobs_types


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
    return []


def get_unique_industries(path):
    data = read(path)
    industries_types = set()
    for industry_type in data:
        if(industry_type['industry'] != ""):
            industries_types.add((industry_type['industry']))
    return industries_types


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
    return []


def get_max_salary(path):
    data = read(path)
    list_salary = []
    for salary in data:
        if(salary['max_salary'] != "" and salary['max_salary'] != 'invalid'):
            list_salary.append(int(salary['max_salary']))
    max_salary = max(list_salary)
    return max_salary


def get_min_salary(path):
    data = read(path)
    list_salary = []
    for salary in data:
        if(salary['min_salary'] != "" and salary['min_salary'] != 'invalid'):
            list_salary.append(int(salary['min_salary']))
    min_salary = min(list_salary)
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

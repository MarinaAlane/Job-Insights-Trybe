from src.jobs import read
from src.helper.get_unique_func import get_unique_list_from_column
from src.helper.filter_by_column import filter_by_column
# from tokenize import Number
# from jobs import read
# from helper.get_unique_func import get_unique_list_from_column


def get_unique_job_types(path):
    jobs_list = read(path)
    data = get_unique_list_from_column(jobs_list, 'job_type')
    return data


def filter_by_job_type(jobs, job_type):
    data = filter_by_column(jobs, job_type, 'job_type')
    return data


def get_unique_industries(path):
    jobs_list = read(path)
    data = get_unique_list_from_column(jobs_list, 'industry')
    return data


def filter_by_industry(jobs, industry):
    data = filter_by_column(jobs, industry, 'industry')
    return data


def get_max_salary(path):
    jobs_list = read(path)
    salary = set()
    for job in jobs_list:
        if job['max_salary'].isnumeric():
            salary.add((int(job['max_salary'])))
            max_salary = max(salary)
    return max_salary


def get_min_salary(path):
    jobs_list = read(path)
    salary = set()
    for job in jobs_list:
        if job['min_salary'].isnumeric():
            salary.add((int(job['min_salary'])))
            min_salary = min(salary)
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

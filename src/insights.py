import math
from src import jobs


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
    all_jobs = jobs.read(path)

    job_types = set()

    for job in all_jobs:
        job_types.add(job["job_type"])

    return job_types


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
    return [job for job in jobs if job["job_type"] == job_type]


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
    all_jobs = jobs.read(path)

    industries = set()

    for job in all_jobs:
        if job["industry"]:
            industries.add(job["industry"])

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
    return [job for job in jobs if job["industry"] == industry]


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
    all_jobs = jobs.read(path)

    highest_max_salary = 0

    for job in all_jobs:
        try:
            max_salary = int(job["max_salary"])

            if max_salary and max_salary > highest_max_salary:
                highest_max_salary = max_salary
        except ValueError:
            pass

    return highest_max_salary


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
    all_jobs = jobs.read(path)

    """
How to set a value to infinite in Python.
Source:
https://stackoverflow.com/questions/7781260/how-can-i-represent-an-infinite-number-in-python
    """
    lowest_min_salary = math.inf

    for job in all_jobs:
        try:
            min_salary = int(job["min_salary"])

            if min_salary and min_salary < lowest_min_salary:
                lowest_min_salary = min_salary
        except ValueError:
            pass

    return lowest_min_salary


def check_key_presence(dictionary, key):
    return key not in dictionary


def is_not_digit(value):
    return type(value) is not int


def check_salary_range(min_value, max_value):
    return min_value > max_value


def check_job_salary_keys(job):
    min_salary = "min_salary"
    max_salary = "max_salary"

    return (
        check_key_presence(job, min_salary)
        or check_key_presence(job, max_salary)
        or is_not_digit(job[min_salary])
        or is_not_digit(job[max_salary])
        or check_salary_range(job[min_salary], job[max_salary])
    )


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
    if check_job_salary_keys(job) or is_not_digit(salary):
        raise (ValueError())

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

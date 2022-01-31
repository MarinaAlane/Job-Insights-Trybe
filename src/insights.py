import csv
from src.jobs import read


def get_unique_job_types(path):
    jobs_types = []
    jobs = read(path)
    for item in jobs:
        if not item["job_type"] in jobs_types:
            jobs_types.append(item["job_type"])
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
    all_jobs = read(path)
    industry_values = set()

    for item in all_jobs:
        if item["industry"] != "":
            industry_values.add(item["industry"])

    return industry_values


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
    with open(path) as jobs:
        max_salary = 0
        all_jobs_list = csv.DictReader(jobs)
        for item in all_jobs_list:
            if item["max_salary"].isdigit():
                if int(item["max_salary"]) > max_salary:
                    max_salary = int(item["max_salary"])
    return max_salary


def get_min_salary(path):
    with open(path) as jobs:
        min_salary = get_max_salary(path)
        all_jobs_list = csv.DictReader(jobs)
        for item in all_jobs_list:
            if item["min_salary"].isdigit():
                if int(item["min_salary"]) < min_salary:
                    min_salary = int(item["min_salary"])
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

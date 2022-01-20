# from jobs import read
from src.jobs import read


def get_unique_job_types(path):
    table = read(path)
    dict_with_all_jobs_title = dict()
    for row in table:
        if row["job_type"] in dict_with_all_jobs_title:
            dict_with_all_jobs_title[row["job_type"]] += 1
        else:
            dict_with_all_jobs_title[row["job_type"]] = 1
    # .. source: https://www.tutorialspoint.com/
    # .. How-to-convert-Python-Dictionary-to-a-list
    list_of_jobs = list(dict_with_all_jobs_title.keys())
    return list_of_jobs


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
    table = read(path)
    dict_with_all_industries = dict()
    for row in table:
        if row["industry"] in dict_with_all_industries:
            dict_with_all_industries[row["industry"]] += 1
        elif len(row["industry"]) > 1:
            dict_with_all_industries[row["industry"]] = 1
    list_of_industries = list(dict_with_all_industries.keys())
    return list_of_industries


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
    pass


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
    pass


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

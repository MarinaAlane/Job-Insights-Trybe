import pprint
from collections import Counter

from src.jobs import read

# from jobs import read

pp = pprint.PrettyPrinter(indent=4)


def get_unique_job_types(path):
    jobs = read(path)
    unique_jobs = Counter(job["job_type"] for job in jobs)
    return list(unique_jobs.keys())


def filter_by_job_type(jobs, job_type):
    specific_job = [
        {"id": job["id"], "job_type": job["job_type"]}
        for job in jobs
        if job["job_type"] == job_type
    ]
    return specific_job


def get_unique_industries(path):
    jobs = read(path)
    unique_industries = Counter(
        job["industry"] for job in jobs if job["industry"]
    )
    ind_list = list(unique_industries.keys())
    return ind_list


def filter_by_industry(jobs, industry):
    filtered_jobs = [job for job in jobs if job["industry"] == industry]
    return filtered_jobs


def get_max_salary(path):
    jobs = read(path)
    max_salary = max(
        int(job["max_salary"]) for job in jobs if job["max_salary"].isdigit()
    )

    return max_salary


# pp.pprint(get_max_salary("src/jobs.csv"))


def get_min_salary(path):
    jobs = read(path)
    min_salary = min(
        int(job["min_salary"]) for job in jobs if job["min_salary"].isdigit()
    )
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

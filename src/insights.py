from multiprocessing.sharedctypes import Value
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
    jobs_list = read(path)
    types_jobs = set()
    for job in jobs_list:
        types_jobs.add(job["job_type"])
    return list(types_jobs)


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
    type_jobs_list = list()
    for job in jobs:
        if job["job_type"] == job_type:
            type_jobs_list.append(job)
    return type_jobs_list


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
    industries = set()
    industries_list = read(path)
    for industry in industries_list:
        if not industry["industry"] == "":
            industries.add(industry["industry"])
    return list(industries)


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
    type_industries_list = list()
    for job in jobs:
        if job["industry"] == industry:
            type_industries_list.append(job)
    return type_industries_list


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
    salaries = list()
    max_salary_list = read(path)
    for salary in max_salary_list:
        if salary["max_salary"].isdigit():
            salaries.append(int(salary["max_salary"]))
    return max(salaries)


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
    salaries = list()
    min_salary_list = read(path)
    for salary in min_salary_list:
        if salary["min_salary"].isdigit():
            salaries.append(int(salary["min_salary"]))
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
    for salaries in job:
        if (
            "min_salary"
            and "max_salary" not in job
            or type(job[salaries]) != int
        ):
            raise ValueError()

        if job["min_salary"] > job["max_salary"] or type(salary) != int:
            raise ValueError()

    return salary >= job["min_salary"] and salary <= job["max_salary"]


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
    job_industries = list()

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                job_industries.append(job)
        except ValueError:
            print("Dados inválidos ou inexistentes")

    return job_industries

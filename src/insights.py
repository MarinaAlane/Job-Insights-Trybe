from src.jobs import read
# from jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    job_types = set()
    for job in jobs_list:
        job_types.add(job["job_type"])
    return job_types
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


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]
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


def get_unique_industries(path):
    jobs_list = read(path)
    industries = set()
    for job in jobs_list:
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries
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
    return []


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]
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
    jobs_list = read(path)
    salaries = []
    for job in jobs_list:
        if job["max_salary"] != "" and job["max_salary"] != "invalid":
            salaries.append(int(job["max_salary"]))
    return max(salaries)
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


def get_min_salary(path):
    jobs_list = read(path)
    salaries = []
    for job in jobs_list:
        if job["min_salary"] != "" and job["min_salary"] != "invalid":
            salaries.append(int(job["min_salary"]))
    return min(salaries)
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

    if not isinstance(salary, int):
        raise ValueError("must inform a valid salary")

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Job must have min and max salary")

    if (
        not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
    ):
        raise ValueError("Min and max salary must be integers")

    if job["min_salary"] > job["max_salary"]:
        raise ValueError("Min salary is greater than max salary")

    return job["min_salary"] <= salary <= job["max_salary"]
    """Checks if a job matches the provided salary range

    Parameters
    ----------
    job : dict
        A job to be checked
    salary : int
        The salary to be checked

    Returns
    -------
    bool
        True if the job matches the salary range, False otherwise
    """
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


def filter_by_salary_range(jobs, salary):
    jobs_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list.append(job)
        except ValueError:
            pass
    return jobs_list

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

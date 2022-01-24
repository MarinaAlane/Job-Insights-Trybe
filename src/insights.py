from src import jobs


def get_unique_job_types(path):
    jobs_data = jobs.read(path)
    unique_job_types = []
    for job in jobs_data:
        if job["job_type"] not in unique_job_types:
            unique_job_types.append(job["job_type"])
    return unique_job_types


def filter_by_job_type(jobs, job_type):
    job_types = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_types.append(job)
    return job_types


def get_unique_industries(path):
    jobs_data = jobs.read(path)
    unique_industries = set()
    for job in jobs_data:
        if job["industry"]:
            unique_industries.add(job["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    industries = []
    for job in jobs:
        if job["industry"] == industry:
            industries.append(job)
    return industries


def get_max_salary(path):
    jobs_data = jobs.read(path)
    max_salary = set()
    for job in jobs_data:
        try:
            if job["max_salary"]:
                max_salary.add(int(job["max_salary"]))
        except ValueError:
            pass
    return max(max_salary)


def get_min_salary(path):
    jobs_data = jobs.read(path)
    min_salary = set()
    for job in jobs_data:
        try:
            if job["min_salary"]:
                min_salary.add(int(job["min_salary"]))
        except ValueError:
            pass
    return min(min_salary)


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

from src.jobs import read


def get_unique_job_types(path):
    jobs_data = read(path)
    job_types = set()

    for job in jobs_data:
        job_types.add(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = [job for job in jobs if job["job_type"] == job_type]

    return filtered_jobs


def get_unique_industries(path):
    jobs_data = read(path)
    job_industry = set()

    for job in jobs_data:
        if job["industry"]:
            job_industry.add(job["industry"])

    return job_industry


def filter_by_industry(jobs, industry):
    filtered_jobs = [job for job in jobs if job["industry"] == industry]

    return filtered_jobs


def get_max_salary(path):
    jobs_data = read(path)
    job_salaries = set()

    for job in jobs_data:
        if job["max_salary"].isnumeric():
            job_salaries.add(int(job["max_salary"]))
    return max(job_salaries)


def get_min_salary(path):
    jobs_data = read(path)
    job_salaries = set()

    for job in jobs_data:
        if job["min_salary"].isnumeric():
            job_salaries.add(int(job["min_salary"]))
    return min(job_salaries)


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

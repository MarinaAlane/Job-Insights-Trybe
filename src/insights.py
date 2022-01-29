import src.jobs as jobs


def get_unique_job_types(path):
    file = jobs.read(path)

    jobs_type = []
    for row in file:
        if row["job_type"] not in jobs_type:
            jobs_type.append(row["job_type"])
    return jobs_type


def filter_by_job_type(jobs, job_type):
    filter_job = []

    for job in jobs:
        if job["job_type"] == job_type:
            filter_job.append(job)
    return filter_job


def get_unique_industries(path):
    list = jobs.read(path)

    industry_type = []
    for row in list:
        if row["industry"] not in industry_type and row["industry"]:
            industry_type.append(row["industry"])
    return industry_type


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
    list = jobs.read(path)

    max_salary = []
    for row in list:
        if row["max_salary"].isnumeric():
            max_salary.append(int(row["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    list = jobs.read(path)

    min_salary = []
    for row in list:
        if row["min_salary"].isnumeric():
            min_salary.append(int(row["min_salary"]))
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

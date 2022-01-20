from src.jobs import read


def get_unique_job_types(path):
    jobs_info = read(path)
    job_type = set()
    for job in jobs_info:
        if job["job_type"] != "":
            job_type.add(job["job_type"])
    return job_type


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job_type == job["job_type"]:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    jobs_info = read(path)
    job_industry = set()
    for job in jobs_info:
        if job["industry"] != "":
            job_industry.add(job["industry"])
    return job_industry


def filter_by_industry(jobs, industry):
    filtered_jobs = []
    for job in jobs:
        if industry == job["industry"]:
            filtered_jobs.append(job)
    return filtered_jobs


def get_max_salary(path):
    jobs_info = read(path)
    max_salary = []
    for job in jobs_info:
        if job["max_salary"]:
            try:
                salary = int(job["max_salary"])
            except ValueError:
                continue
            max_salary.append(salary)
    return max(max_salary)


def get_min_salary(path):
    jobs_info = read(path)
    min_salary = []
    for job in jobs_info:
        if job["min_salary"]:
            try:
                salary = int(job["min_salary"])
            except ValueError:
                continue
            min_salary.append(salary)
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

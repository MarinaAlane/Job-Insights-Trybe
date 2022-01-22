from src.jobs import read


def get_unique_job_types(path):

    all_jobs = read(path)
    unique_job_titles = set()
    for job in all_jobs:
        unique_job_titles.add(job["job_type"])
    return unique_job_titles


def filter_by_job_type(jobs, job_type):
    jobs_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_list.append(job)
    return jobs_list


def get_unique_industries(path):
    all_jobs = read(path)
    unique_industries = set()
    for job in all_jobs:
        if len(job["industry"]) > 0:
            unique_industries.add(job["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    jobs_list = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_list.append(job)
    return jobs_list


def get_max_salary(path):
    all_jobs = read(path)
    all_jobs_filter = []
    for job in all_jobs:
        if len(job["max_salary"]) > 5:
            all_jobs_filter.append(job["max_salary"])
    ints = [int(item) for item in all_jobs_filter]
    max_salary = max(ints)
    return max_salary

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
    all_jobs = read(path)
    all_jobs_filter = []
    for job in all_jobs:
        if len(job["min_salary"]) > 0:
            all_jobs_filter.append(job["min_salary"])
    ints = [int(item) for item in all_jobs_filter]
    min_salary = min(ints)
    return min_salary
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

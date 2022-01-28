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
    this_set = set()
    this_dic = read(path)
    for row in this_dic:
        this_set.add(row["job_type"])
    return this_set


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
    REF:. https://stackoverflow.com/questions/
    8653516/python-list-of-dictionaries-search
    REF:. https://www.w3schools.com/python/python_lambda.asp
    """
    return list(filter(lambda teste: teste['job_type'] == job_type, jobs))


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
    this_set = set()
    this_dic = read(path)
    for row in this_dic:
        this_set.add(row["industry"])
    this_set = list(filter(None, this_set))
    return this_set


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
    return list(filter(lambda teste: teste['industry'] == industry, jobs))


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
    this_set = set()
    this_dic = read(path)
    for row in this_dic:
        if row["max_salary"].isnumeric():
            this_set.add(int(row["max_salary"]))
    maxxx = max(this_set)
    return maxxx


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
    this_set = set()
    this_dic = read(path)
    for row in this_dic:
        if row["min_salary"].isnumeric():
            this_set.add(int(row["min_salary"]))
    minnn = min(this_set)
    return minnn


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
    a = 'max_salary'
    b = 'min_salary'
    if (
        a in job
            and b in job
            and isinstance(job[a], int)
            and isinstance(job[b], int)
            and job[b] < job[a]
            and isinstance(salary, int)):
        if job[a] > salary >= job[b]:
            return True
        return False
    raise ValueError("KeyError: 'max_salary'")


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
    if not isinstance(salary, int):
        return []
    a = 'max_salary'
    b = 'min_salary'
    x = list(
        filter(
            lambda teste: teste[a] > salary >= teste[b], jobs
            ))
    return x

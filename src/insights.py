from . import jobs


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
    result = set()
    data = jobs.read(path)
    for job in data:
        result.add(job["job_type"])
    return result


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
    return [j for j in jobs if j["job_type"] == job_type]


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
    result = set()
    data = jobs.read(path)
    for job in data:
        if "industry" in job:
            if job["industry"] != "":
                result.add(job["industry"])
    return result


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
    return [j for j in jobs if "industry" in j and j["industry"] == industry]


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
    data = jobs.read(path)
    max_salary = 0
    for job in data:
        if "max_salary" in job:
            if job["max_salary"] != "" and job["max_salary"].isnumeric():
                if int(job["max_salary"]) > max_salary:
                    max_salary = int(job["max_salary"])
    return max_salary


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
    data = jobs.read(path)
    min_salary = get_max_salary(path)
    for job in data:
        if "min_salary" in job:
            if job["min_salary"] != "" and job["min_salary"].isnumeric():
                if int(job["min_salary"]) < min_salary:
                    min_salary = int(job["min_salary"])
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
    if not isinstance(salary, int):
        raise ValueError
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    if (type(job["min_salary"]) is not int or
            type(job["max_salary"]) is not int):
        raise ValueError
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError
    return job["max_salary"] >= salary >= job["min_salary"]


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
    result = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                result.append(job)
        except ValueError:
            pass
    return result

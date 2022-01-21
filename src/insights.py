from src.jobs import read
# from jobs import read


def get_unique_job_types(path):
    get_read = read(path)
    job_types = []

    for res in get_read:
        if res["job_type"] not in job_types:
            job_types.append(res["job_type"])

    return job_types


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
    return []


def get_unique_industries(path):
    get_read = read(path)
    unique_industries = []

    for res in get_read:
        if res["industry"] \
          not in unique_industries \
          and len(res["industry"]) != 0:
            unique_industries.append(res["industry"])

    return unique_industries


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
    get_read = read(path)
    max_salary = 0

    for res in get_read:
        if len(res["max_salary"]) \
          and res["max_salary"].isnumeric():
            salary = int(res["max_salary"])
            if salary > max_salary:
                max_salary = salary

    return max_salary


def get_min_salary(path):
    get_read = read(path)
    min_salary = 9999999

    for res in get_read:
        if len(res["min_salary"]) \
          and res["min_salary"].isnumeric():
            salary = int(res["min_salary"])
            if salary < min_salary:
                min_salary = salary

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

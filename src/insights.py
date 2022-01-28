from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    res = list(set(job['job_type'] for job in data))

    return res


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
    data = read(path)

    all_industries = list(set(job['industry'] for job in data))
    industries = list(filter(None, all_industries))

    return industries


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
    data = read(path)

    max_salary_list = filter(
        None,
        list(set(job['max_salary'] for job in data))
    )
    filter_list = filter(
        lambda value: value.isnumeric(),
        list(max_salary_list)
    )

    integer_list = list(map(int, filter_list))
    max_salary = max(integer_list)

    return max_salary


def get_min_salary(path):
    data = read(path)

    min_salary_list = filter(
        None,
        list(set(job['min_salary'] for job in data))
    )
    filter_list = filter(
        lambda value: value.isnumeric(),
        list(min_salary_list)
    )

    integer_list = list(map(int, filter_list))
    min_salary = min(integer_list)

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

from src.jobs import read


def get_unique_job_types(path):
    get_jobs_data = read(path)
    result = set()
    for get_job_data in get_jobs_data:
        result.add(get_job_data["job_type"])

    return list(result)


def filter_by_job_type(jobs, job_type):
    # para realizar o requisito, utilizei o auxilio de seguinte material:
    # https://www.programiz.com/python-programming/methods/built-in/filter
    filtered_jobs = filter(lambda job: (job["job_type"] == job_type), jobs)

    return list(filtered_jobs)


def get_unique_industries(path):
    get_industries_data = read(path)
    result = []
    for get_industry_data in get_industries_data:
        if get_industry_data["industry"] != "":
            result.append(get_industry_data["industry"])

    return set(result)


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
    get_salaries_data = read(path)
    result = set()

    for get_salary_data in get_salaries_data:
        try:
            result.add(int(get_salary_data["max_salary"]))
        except ValueError:
            pass

    return max(result)


def get_min_salary(path):
    get_salaries_data = read(path)
    result = set()

    for get_salary_data in get_salaries_data:
        try:
            result.add(int(get_salary_data["min_salary"]))
        except ValueError:
            pass

    return min(result)


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

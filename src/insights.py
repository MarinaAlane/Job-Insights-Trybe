from src.jobs import read


def get_distinct_values_by_key(job_list, key):
    results = [job[key] for job in job_list if job[key]]

    return list(set(results))


def get_unique_job_types(path):
    jobs = read(path)

    return get_distinct_values_by_key(jobs, 'job_type')


def filter_by_job_type(jobs, job_type):
    if job_type == '':
        return list()

    return [job for job in jobs if job['job_type'] == job_type]


def get_unique_industries(path):
    jobs = read(path)

    return get_distinct_values_by_key(jobs, 'industry')


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
    jobs = read(path)
    salaries = get_distinct_values_by_key(jobs, 'max_salary')
    max_salary = 0

    for salary in salaries:
        if salary.isdigit() and float(salary) > float(max_salary):
            max_salary = salary
    return float(max_salary)


def get_min_salary(path):
    jobs = read(path)
    salaries = get_distinct_values_by_key(jobs, 'min_salary')
    min_salary = 0.00

    for i, salary in enumerate(salaries):
        if i == 0:
            min_salary = salary
        elif salary.isdigit() and float(salary) < float(min_salary):
            min_salary = salary
    return float(min_salary)


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

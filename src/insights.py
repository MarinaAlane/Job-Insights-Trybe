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
    jobs = read(path)
    job_types = set()

    for job in jobs:
        job_types.add(job['job_type'])

    return list(job_types)


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
    return [job for job in jobs if job['job_type'] == job_type]


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
    jobs = read(path)
    industries = set()

    for job in jobs:
        if job['industry'] != '':
            industries.add(job['industry'])

    return list(industries)


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
    return [job for job in jobs if job['industry'] == industry]


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
    jobs = read(path)
    salary = list()

    for job in jobs:
        if job['max_salary'].isnumeric():
            salary.append(int(job['max_salary']))

    salary.sort(reverse=True)

    return salary[0]


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
    jobs = read(path)
    salary = list()

    for job in jobs:
        if job['min_salary'].isnumeric():
            salary.append(int(job['min_salary']))

    return min(salary)


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

    ERRORS = {
        'missing_key': 'Keys "min_salary" or "max_salary" doesn\'t exists',
        'not_str': 'Keys "min_salary" or "max_salary" not a number',
        'inconsistent_values': '"min_salary" is greather than "max_salary"',
        'invalid_salary': '"salary" isn\'t a valid integer',
    }

    if 'min_salary' not in job.keys() or 'max_salary' not in job.keys():
        raise ValueError(ERRORS['missing_key'])

    # https://www.w3schools.com/python/ref_func_isinstance.asp
    if (
        not isinstance(job['min_salary'], int) or
        not isinstance(job['max_salary'], int)
    ):
        raise ValueError(ERRORS['not_str'])

    if job['min_salary'] > job['max_salary']:
        raise ValueError(ERRORS['inconsistent_values'])

    if not isinstance(salary, int):
        raise ValueError(ERRORS['invalid_salary'])

    return job['min_salary'] <= salary <= job['max_salary']


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

    filtered_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass

    return filtered_jobs

from src.jobs import read


def get_unique_job_types(path):
    jobs_csv = read(path)
    jobs_cvs_types = set()
    for value_csv in jobs_csv:
        for job_index in value_csv["job_type"].split(","):
            jobs_cvs_types.add(job_index)
    return jobs_cvs_types


def filter_by_job_type(jobs, job_type):
    jobs_Types = []
    for job in jobs:
        if job['job_type'] == job_type:
            jobs_Types.append(job)
    return jobs_Types


def get_unique_industries(path):
    jobs = read(path)
    industries = set()
    for i in jobs:
        industry = i["industry"]
        if (industry != ''):
            industries.add(industry)
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
    arr_csv = read(path)
    max_salaries = []
    for item in arr_csv:
        if (item['max_salary'] != '' and item['max_salary'] != 'invalid'):
            max_salaries.append(int(item['max_salary']))
    max_salaries.sort()
    return max_salaries[-1]
# Rodolfo Rezende me ajudou na resolução dessa função


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

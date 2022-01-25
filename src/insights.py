from src.jobs import read


def get_unique_job_types(path):
    jobs_csv = read(path)
    job_types_from_csv = set()

    for job in jobs_csv:
        job_types_from_csv.add(job["job_type"])
              
    return job_types_from_csv


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
    jobs_industries_csv = read(path)
    job_industry_from_csv = set()

    for job in jobs_industries_csv["industry"]:
        job_industry_from_csv.add(job["industry"])

    return job_industry_from_csv


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
    jobs_salaries_csv = read(path)
    job_salary_from_csv = set()

    for job in jobs_salaries_csv["max_salary"]:
        if job:
            job_salary_from_csv.add(int(job["max_salary"]))

    return max(job_salary_from_csv)


def get_min_salary(path):
    jobs_salaries_csv = read(path)
    job_salary_from_csv = set()

    for job in jobs_salaries_csv["min_salary"]:
        if job:
            job_salary_from_csv.add(int(job["min_salary"]))

    return min(job_salary_from_csv)


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

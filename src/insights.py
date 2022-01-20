from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    unique_jobs = set()
    for job in jobs:
        unique_jobs.add(job["job_type"])
    return unique_jobs


def filter_by_job_type(jobs, job_type):
    return [job
            for job in jobs
            if job["job_type"] == job_type]


def get_unique_industries(path):
    jobs = read(path)
    unique_industries = set()
    for job in jobs:
        industry = job["industry"].strip()
        if not industry == '':
            unique_industries.add(industry)
    return unique_industries


def filter_by_industry(jobs, industry):
    return [job
            for job in jobs
            if job["industry"] == industry]


def get_max_salary(path):
    jobs = read(path)

    salaries = [job["max_salary"]
                for job in jobs
                if job["max_salary"].strip() != ''
                and job["max_salary"] != 'invalid']

    max_salaries = set()
    for salary in salaries:
        salaryNumber = int(salary)
        max_salaries.add(salaryNumber)

    return max(max_salaries)


def get_min_salary(path):
    jobs = read(path)

    salaries = [job["min_salary"]
                for job in jobs
                if job["min_salary"].strip() != ''
                and job["min_salary"] != 'invalid']

    min_salaries = set()
    for salary in salaries:
        salaryNumber = int(salary)
        min_salaries.add(salaryNumber)

    return min(min_salaries)


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

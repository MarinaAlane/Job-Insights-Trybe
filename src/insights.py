from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    jobs_types = set()
    for job in jobs_list:
        jobs_types.add(job["job_type"])
    return jobs_types


def filter_by_job_type(jobs, job_type):
    #  o primeiro parametro que recebe já é uma lista
    list_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:  # se for = ao do parametro
            list_jobs.append(job)
    return list_jobs


def get_unique_industries(path):
    fileContent = read(path)
    industries = set()
    for industry in fileContent:
        if industry["industry"] != '':
            industries.add(industry["industry"])
    return industries


def filter_by_industry(jobs, industry):
    #  o primeiro parametro que recebe já é uma lista
    list_industries = []
    for job in jobs:
        if job["industry"] == industry:  # se for = ao do parametro
            list_industries.append(job)
    return list_industries


def get_max_salary(path):
    fileContent = read(path)
    max_salary = 0
    for salary in fileContent:
        payment = salary["max_salary"]
        if payment != '' and payment != 'invalid':
            if int(payment) > int(max_salary):
                max_salary = payment
    return int(max_salary)


def get_min_salary(path):
    fileContent = read(path)
    min_salary = []
    for salary in fileContent:
        payment = salary["min_salary"]
        if payment != '' and payment != 'invalid':
            min_salary.append(int(payment))
    return min(min_salary)

# Referencia para utilziação da função min:
# https://www.w3schools.com/python/ref_func_min.asp


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

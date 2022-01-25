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
    if type(salary) is not int:
        raise ValueError('Salary isnt a value integer')
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError('min_salary or max_salary dosent exists')
    if (
        type(job["max_salary"]) is not int
        or type(job["min_salary"]) is not int
      ):
        raise ValueError('min_salary or max_salary arent valid integer')
    return job["mix_salary"] <= salary <= job["max_salary"]


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

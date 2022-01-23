from .jobs import read


def get_unique_job_types(path):
    job_data = read(path)
    job_types = set()
    for job in job_data:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_by_job_type = [job for job in jobs if job["job_type"] == job_type]
    return filtered_by_job_type


def get_unique_industries(path):
    job_data = read(path)
    job_industry = set()
    for job in job_data:
        if job["industry"] != "":
            job_industry.add(job["industry"])
    return job_industry


def filter_by_industry(jobs, industry):
    filtered_by_industry = [job for job in jobs if job["industry"] == industry]
    return filtered_by_industry


def get_max_salary(path):
    job_data = read(path)
    job_salary = set()
    for job in job_data:
        if job["max_salary"].isnumeric():
            job_salary.add(int(job["max_salary"]))
    return max(job_salary)


def get_min_salary(path):
    job_data = read(path)
    job_salary = set()
    for job in job_data:
        if job["min_salary"].isnumeric():
            job_salary.add(int(job["min_salary"]))
    return min(job_salary)

# Consulta na documentação e materials para compreensão de lançamento de erros
#  e também sobre o  'not in':
# https://docs.python.org/pt-br/3.8/tutorial/errors.html
# https://www.w3schools.com/python/python_operators.asp
# http://excript.com/python/operadores-in-not-in-python.html


def matches_salary_range(job, salary):

    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError
    if (
        type(salary) != int
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
    ):
        raise ValueError

    if job["min_salary"] > job["max_salary"]:
        raise ValueError()

    return job["min_salary"] <= salary <= job["max_salary"]


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

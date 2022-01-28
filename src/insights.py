# from multiprocessing.sharedctypes import Value
from .jobs import read


def get_unique_job_types(path):
    data = read(path)
    jobs_type_index = set()
    for index in data:
        jobs_type_index.add(index["job_type"])
    return list(jobs_type_index)


def filter_by_job_type(jobs, job_type):
    data = []
    for job in jobs:
        if job["job_type"] == job_type:
            data.append(job)
    return data

    # return [job for job in jobs if job['job_type'] == job_type]


def get_unique_industries(path):
    data = read(path)
    industry_type_index = set()
    for index in data:
        if index["industry"] != "":
            industry_type_index.add(index["industry"])
    return list(industry_type_index)


# print(get_unique_industries("jobs.csv"))


def filter_by_industry(jobs, industry):
    data = []
    for job in jobs:
        if job["industry"] == industry:
            data.append(job)
    return data
    # print(jobs)
    # print('aaaaaa', industry)
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
    max_salary = set()
    for index in data:
        if index["max_salary"].isdigit():
            max_salary.add(int(index["max_salary"]))
    return max(list(max_salary))

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
    pass


def get_min_salary(path):
    data = read(path)
    min_salary = set()
    for index in data:
        if index["min_salary"].isdigit():
            min_salary.add(int(index["min_salary"]))
    return min(list(min_salary))
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


def matches_salary_range(job, salary):
    max_salary, min_salary = job.get("max_salary"), job.get("min_salary")
    if type(max_salary) != int or type(min_salary) != int:
        raise ValueError
    elif max_salary < min_salary:
        raise ValueError
    elif type(salary) != int:
        raise ValueError
    elif min_salary <= salary <= max_salary:
        return True
    return False

    # lembrar de perguntar sobre a função isinstance e o porque ela não
    # estava funcionando! o que ela retorna!
    #  também perguntar como fazer as coisas com try e se
    # dava pra fazer de outra forma,
    #  e como quebrar linhas em um if
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
    lista = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                lista.append(job)
        except ValueError:
            pass
    return lista


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

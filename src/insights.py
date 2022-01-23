from src import jobs


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

    data = jobs.read(path)

    job_types = set()  # cria listas sem elementos duplicados
    for job in data:
        job_types.add(job["job_type"])

    return job_types


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

    return [job for job in jobs if job["job_type"] == job_type]


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
    data = jobs.read(path)

    industries = set()  # cria listas sem elementos duplicados
    for industry in data:
        if industry["industry"] != "":  # retira a linha em branco
            industries.add(industry["industry"])

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
    return [ind_type for ind_type in jobs if ind_type["industry"] == industry]


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

    data = jobs.read(path)

    highest_salary = 0  # menor valor possível

    for salary in data:   # itera os nũmeros da data
        if "max_salary" in salary:  # validaçao - sugestão slack erro int
            max = salary["max_salary"]
            if max.isnumeric() and int(max) > highest_salary:
                highest_salary = int(max)  # se maior o substitui

    return highest_salary


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
    data = jobs.read(path)

    min_salary = float("inf")  # maior valor possível

    for salary in data:  # itera os nũmeros da data
        if "min_salary" in salary:  # validaçao - sugestão slack erro int
            min = salary["min_salary"]
            if min.isnumeric() and int(min) < min_salary:
                min_salary = int(min)  # se menor que a atribuição o substitui

    return min_salary


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

    if not isinstance(job.get("min_salary"), int):
        raise ValueError  # get() checa se a key existe no dicionãrio
    if not isinstance(job.get("max_salary"), int):
        raise ValueError
    if job["min_salary"] > job["max_salary"]:
        raise ValueError
    if not isinstance(salary, int):
        raise ValueError  # verifica se o objeto específico é do tipo indicado
    return job["max_salary"] >= salary >= job["min_salary"]


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


#  max - https://www.delftstack.com/pt/howto/python/python-max-value-in-list/
#  https://pt.stackoverflow.com/questions/216771/como-obter-o-menor-valor-em-uma-lista
# https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not

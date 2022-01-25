def get_unique_job_types(path):
    from src.jobs import read

    content = read(path)

    types = set()  # Conjuto de Jobs
    # Referencia do comando Pass:
    # www.delftstack.com/pt/howto/python/python-pass/#:text=A%20instru%C3%A7%C3%A3o%20pass%20%C3%A9%20usada,que%20o%20programa%20fa%C3%A7a%20nada.
    for job in content:
        if job["job_type"] in types:
            pass
        else:
            types.add(job["job_type"])
    return types


def filter_by_job_type(jobs, job_type):
    filtered_job_types = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_job_types.append(job)
    return filtered_job_types


def get_unique_industries(path):
    from src.jobs import read

    content = read(path)

    industries = set()

    for job in content:
        if job["industry"] == "":  # Excluindo registros vazios
            pass
        else:
            industries.add(job["industry"])
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
    from src.jobs import read

    content = read(path)

    get_salaries = set()

    for job in content:
        if job["max_salary"]:
            try:
                get_salaries.add(int(job["max_salary"]))
            except ValueError:
                continue  # gerando exceção para valor não-inteiro
    return max(get_salaries)


def get_min_salary(path):
    from src.jobs import read

    content = read(path)

    get_salaries = set()

    for job in content:
        if job["min_salary"]:
            try:
                get_salaries.add(int(job["min_salary"]))
            except ValueError:
                continue
    return min(get_salaries)


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

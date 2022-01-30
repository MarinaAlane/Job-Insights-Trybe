from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    jobs_type = []
    # Se não tiver a linha job_type dentro do array vazio, é adicionado ao
    # array

    for row in data:
        if row["job_type"] not in jobs_type:
            jobs_type.append(row["job_type"])
    return jobs_type


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    # Verifica o job_types do jobs, e adiciona na lista.
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):

    content = read(path)
    industries = []
    # A cada linha verifica se não existe 'industry' dentro do array e
    # se não é vazio então coloca dentro do array industries
    for row in content:
        if row["industry"] not in industries and row["industry"] != "":
            industries.append(row["industry"])
    return industries


def filter_by_industry(jobs, industry):
    filtered_industries = []
    # Verifica o job_types do jobs, e adiciona na lista.
    for job in jobs:
        if job["industry"] == industry:
            filtered_industries.append(job)
    return filtered_industries


def get_max_salary(path):
    content = read(path)
    salaries = []
    # A cada linha verifica se o max_salary é um dígito,
    # e adiciona na lista salaries.
    # colocando como inteiro e retorna a lista
    for row in content:
        if row["max_salary"].isdigit():
            salaries.append(int(row["max_salary"]))
    return max(salaries)


def get_min_salary(path):

    content = read(path)
    salaries = []
    # A cada linha verifica se o min_salary é um dígito, e adiciona
    # na lista salaries, colocando como inteiro e retorna a lista
    for row in content:
        if row["min_salary"].isdigit():
            salaries.append(int(row["min_salary"]))
    return min(salaries)


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

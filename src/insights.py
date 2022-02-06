from src import jobs


def get_unique_job_types(path):
    # utiliza a função feita no requisito 1
    data = jobs.read(path)

    # cria um set, pois se trata de um conjunto de elementos unicos
    types_of_jobs = set()
    for job in data:
        types_of_jobs.add(job["job_type"])
    return types_of_jobs


def filter_by_job_type(jobs, job_type):
    selected_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            selected_jobs.append(job)

    return selected_jobs


def get_unique_industries(path):
    data = jobs.read(path)
    industries = set()

    for job in data:
        if job["industry"]:
            industries.add(job["industry"])

    return industries


def filter_by_industry(jobs, industry):
    selected_industries = []
    for job in jobs:
        if job["industry"] == industry:
            selected_industries.append(job)

    return selected_industries


def get_max_salary(path):
    data = jobs.read(path)
    salaries = []

    for job in data:
        salary = job["max_salary"]
        if salary.isdigit():
            salaries.append(int(salary))

    return max(salaries)


def get_min_salary(path):
    data = jobs.read(path)
    salaries = []

    for job in data:
        salary = job["min_salary"]
        if salary.isdigit():
            salaries.append(int(salary))

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

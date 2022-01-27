from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_types = set()
    for job in jobs:
        if job['job_type'] != '':
            job_types.add(job['job_type'])
    return list(job_types)


# Solução para filtrar encontrada em:
# https://stackoverflow.com/questions/32474022/filter-list-of-dictionaries
def filter_by_job_type(jobs, job_type):
    if job_type == '':
        return []
    filtered_job_type = [job for job in jobs if job['job_type'] == job_type]
    return filtered_job_type


# Solução if encontrada em:
# https://stackoverflow.com/questions/54866974/
# what-is-efficient-way-of-removing-empty-values-from-dict-inside-list/54867063
def get_unique_industries(path):
    jobs = read(path)
    industry_types = set()
    for job in jobs:
        if job['industry'] != '':
            industry_types.add(job['industry'])
    return list(industry_types)


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
    jobs = read(path)
    higher_salary = set()
    for salary in jobs:
        if salary['max_salary'].isdigit():
            higher_salary.add(int((salary['max_salary'])))
    return max(list(higher_salary))


def get_min_salary(path):
    jobs = read(path)
    lower_salary = set()
    for salary in jobs:
        if salary['min_salary'].isdigit():
            lower_salary.add(int((salary['min_salary'])))
    return min(list(lower_salary))


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

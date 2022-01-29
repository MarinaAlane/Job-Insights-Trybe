from src.jobs import read


def get_unique_job_types(path):
    listaUnica = read(path)
    job_type = []

    for row in listaUnica:
        if job_type.__contains__(row['job_type']) is False:
            job_type.append(row['job_type'])
    return job_type


def filter_by_job_type(jobs, job_type):

    list_job = [row for row in jobs if row['job_type'] == job_type]
    return list_job


def get_unique_industries(path):
    valore_unicos = read(path)
    ind = []
    bo = False

    for row in valore_unicos:
        if ind.__contains__(row['industry']) == bo and row['industry'] != '':
            ind.append(row['industry'])
    return ind


get_unique_industries('src/jobs.csv')


def filter_by_industry(jobs, industry):
    list_job = [row for row in jobs if row['industry'] == industry]
    return list_job


def get_max_salary(path):
    valore_unicos = read(path)
    max_s = set()

    for row in valore_unicos:
        if row['max_salary'] != '' and row['max_salary'] != 'invalid':
            max_s.add(int(row['max_salary']))

    return max(max_s)
    pass


def get_min_salary(path):
    valore_unicos = read(path)
    max_s = set()

    for row in valore_unicos:
        if row['min_salary'] != '' and row['min_salary'] != 'invalid':
            max_s.add(int(row['min_salary']))

    return min(max_s)
    pass


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

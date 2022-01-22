from src.jobs import read


def get_unique_job_types(path):
    jobs_csv = read(path)
    jobs_types_list = []
    for job in jobs_csv:
        if job["job_type"] not in jobs_types_list:
            jobs_types_list.append(job["job_type"])
    return jobs_types_list


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
    return []


# SET: https://www.w3schools.com/python/ref_func_set.asp
# ADD: https://www.w3schools.com/python/ref_set_add.asp
# usando set() para pegar valores unicos
# usando ADD pois funciona com set(), pois append() não funciona.
def get_unique_industries(path):
    jobs_csv = read(path)
    industry_list = set()
    for job in jobs_csv:
        if job["industry"] != "":
            industry_list.add(job["industry"])
    return industry_list


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


# usando a condição para não puxar valores vazios ocorre erro:
# ValueError: invalid literal for int() with base 10: 'invalid'
# ISNUMERIC() -> usado para evitar esse problema.
# https://www.w3schools.com/python/ref_string_isnumeric.asp
def get_max_salary(path):
    jobs_csv = read(path)
    max_salary = 0
    for job in jobs_csv:
        if job["max_salary"].isnumeric():
            if int(job["max_salary"]) > max_salary:
                max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path):
    """ asdasdasd """


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

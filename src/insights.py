from .jobs import read


def get_unique_list(path, key):
    jobs = read(path)
    new_set = set()

    for item in jobs:
        if item[f"{key}"] != "":
            new_set.add(item[f"{key}"])

    return new_set


def get_unique_job_types(path):
    result = get_unique_list(path, "job_type")
    return result


def filter_by_job_type(jobs, job_type):
    jobs_by_type = list()
    for offer in jobs:
        if offer["job_type"] == job_type:
            jobs_by_type.append(offer)

    return jobs_by_type


def get_unique_industries(path):
    result = get_unique_list(path, "industry")
    return result


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
    salaries = get_unique_list(path, "max_salary")
    biggest_salary = 0
    salaries_list = list()
    for salary in salaries:
        if salary.isnumeric():
            salaries_list.append(int(salary))

    for salary in salaries_list:
        if salary >= biggest_salary:
            biggest_salary = salary
    return biggest_salary


def get_min_salary(path):
    salaries = get_unique_list(path, "min_salary")
    salaries_list = list()
    for salary in salaries:
        if salary.isnumeric():
            salaries_list.append(int(salary))

    smallest_salary = salaries_list[0]
    for salary in salaries_list:
        if salary <= smallest_salary:
            smallest_salary = salary
    return smallest_salary


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

# python3 -m pytest -k nome_da_func_de_tests
# get_max_salary("/home/silva_enilsom/trybe/projetos/sd-011-project-job-insights/src/jobs.csv")

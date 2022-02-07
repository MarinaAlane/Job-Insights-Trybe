from src.jobs import read


def get_unique_job_types(path):
    data = read(path)

    job_types = set()
    for row in data:
        job_types.add(row["job_type"])

    return list(job_types)


def filter_by_job_type(jobs, job_type):
    filtered = []
    for job in jobs:
        if job['job_type'] == job_type:
            filtered.append(job)

    return filtered


def get_unique_industries(path):
    data = read(path)

    industries = set()
    for row in data:
        industry = row["industry"]
        if industry:
            industries.add(industry)

    return list(industries)


def filter_by_industry(jobs, industry):
    filtered = []
    for job in jobs:
        if job['industry'] == industry:
            filtered.append(job)

    return filtered


def get_max_salary(path):
    datas = read(path)

    max_salaries = list()
    for data in datas:
        salary = data["max_salary"]
        if salary.isdigit():
            max_salaries.append(int(salary))

    return max(max_salaries)


def get_min_salary(path):
    datas = read(path)

    min_salaries = list()
    for data in datas:
        salary = data["min_salary"]
        if salary.isdigit():
            min_salaries.append(int(salary))

    return min(min_salaries)


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

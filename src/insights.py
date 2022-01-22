from src.jobs import read


def get_unique_job_types(path):
    csv = read(path)
    job_type = set()
    for row in csv:
        job_type.add(row["job_type"])
    return job_type


def filter_by_job_type(jobs, job_type):
    filter_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filter_jobs.append(job)
    return filter_jobs


def get_unique_industries(path):
    csv = read(path)
    list = set()
    for item in csv:
        industry = item["industry"]
        if industry != '':
            list.add(industry)
    return list


def filter_by_industry(jobs, industry):
    filter_industry = []
    for job in jobs:
        if job["industry"] == industry:
            filter_industry.append(job)
    return filter_industry


def get_max_salary(path):
    csv = read(path)
    higher_salary = 0
    for item in csv:
        max_salary = item["max_salary"]
        if max_salary != '' and max_salary != 'invalid':
            if int(max_salary) > int(higher_salary):
                higher_salary = max_salary
    return int(higher_salary)


def get_min_salary(path):
    csv = read(path)
    salaries = []
    for item in csv:
        min_salary = item["min_salary"]
        if min_salary != '' and min_salary != 'invalid':
            salaries.append(int(min_salary))
    salaries.sort()
    return salaries[0]


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

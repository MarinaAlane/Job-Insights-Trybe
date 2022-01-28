from src.jobs import read
arrayjobs = read("src/jobs.csv")


def get_unique_job_types(path):
    job_types = read(path)
    list_types = []
    for row in job_types:
        if row["job_type"] not in list_types:
            list_types.append(row["job_type"])
    return list_types


def filter_by_job_type(jobs, job_type):
    filter_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filter_jobs.append(job)
    return filter_jobs


def get_unique_industries(path):
    industries = read(path)
    list_industry = []
    for row in industries:
        if row["industry"] not in list_industry and row["industry"] != '':
            list_industry.append(row["industry"])
    return list_industry


def filter_by_industry(jobs, industry):
    filter_industries = []
    for job in jobs:
        if job["industry"] == industry:
            filter_industries.append(job)
            print(job)
    return filter_industries


""" função max consultada no site
https://www.delftstack.com"""


def get_max_salary(path):
    salary = read(path)
    bigger_salary = []
    for row in salary:
        if row["max_salary"].isdigit() and row["max_salary"] != "":
            bigger_salary.append(int(row["max_salary"]))
    return max(bigger_salary)


def get_min_salary(path):
    salary = read(path)
    smaller_salary = []
    for row in salary:
        if row["min_salary"].isdigit() and row["min_salary"] != "":
            smaller_salary.append(int(row["min_salary"]))
    return min(smaller_salary)


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

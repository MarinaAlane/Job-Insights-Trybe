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
    if ("min_salary" not in job or "max_salary" not in job):
        raise ValueError
    elif (
        isinstance(job["min_salary"], int) is not True
        or isinstance(job["max_salary"], int) is not True
        or job["min_salary"] >= job["max_salary"]
        or isinstance(salary, int) is not True
    ):
        raise ValueError
    elif (
        job["min_salary"] <= salary <= job["max_salary"]
    ):
        return True
    else:
        return False
       

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

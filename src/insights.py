from src.jobs import read


def get_unique_job_types(path):
    data_job = read(path)
    job_types = set()
    for data in data_job:
        job_types.add(data["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    filter_job = list(filter(lambda job: job["job_type"] == job_type, jobs))

    return filter_job


def get_unique_industries(path):
    list_jobs = read(path)
    job_industry = set()
    for job in list_jobs:
        if job['industry'] != "":
            job_industry.add(job['industry'])

    return job_industry


def filter_by_industry(jobs, industry):
    filt_industry = list(filter(lambda job: job["industry"] == industry, jobs))

    return filt_industry


def get_max_salary(path):
    data_job = read(path)
    salary = set()
    for job in data_job:
        if job["max_salary"].isnumeric():
            salary.add(int(job["max_salary"]))

    return max(salary)


def get_min_salary(path):
    data_job = read(path)
    salary = set()
    for job in data_job:
        if job["min_salary"].isnumeric():
            salary.add(int(job["min_salary"]))

    return min(salary)


def matches_salary_range(job, salary):
    if ("min_salary" or "max_salary" not in job):
        raise ValueError
    elif (
        type(job["min_salary"]) != int or
        type(job["max_salary"]) != int or
        type(salary) != int
    ):
        raise ValueError
    elif (job["min_salary"] > job["max_salary"]):
        raise ValueError
    elif (job["min_salary"] <= salary <= job["max_salary"]):
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

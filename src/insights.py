from src.jobs import read


def get_unique_job_types(path):
    jobs_info = read(path)
    job_type = set()
    for job in jobs_info:
        if job["job_type"] != "":
            job_type.add(job["job_type"])
    return job_type


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job_type == job["job_type"]:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    jobs_info = read(path)
    job_industry = set()
    for job in jobs_info:
        if job["industry"] != "":
            job_industry.add(job["industry"])
    return job_industry


def filter_by_industry(jobs, industry):
    filtered_jobs = []
    for job in jobs:
        if industry == job["industry"]:
            filtered_jobs.append(job)
    return filtered_jobs


def get_max_salary(path):
    jobs_info = read(path)
    max_salary = []
    for job in jobs_info:
        if job["max_salary"]:
            try:
                salary = int(job["max_salary"])
            except ValueError:
                continue
            max_salary.append(salary)
    return max(max_salary)


def get_min_salary(path):
    jobs_info = read(path)
    min_salary = []
    for job in jobs_info:
        if job["min_salary"]:
            try:
                salary = int(job["min_salary"])
            except ValueError:
                continue
            min_salary.append(salary)
    return min(min_salary)


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError
    if (
        not type(job["max_salary"]) is int
        or not type(job["min_salary"]) is int
        or not type(salary) is int
    ):
        raise ValueError
    if job["max_salary"] < job["min_salary"]:
        raise ValueError
    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
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

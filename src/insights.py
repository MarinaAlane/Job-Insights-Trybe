from src.jobs import read


def get_unique_job_types(path):

    all_jobs = read(path)
    unique_job_titles = set()
    for job in all_jobs:
        unique_job_titles.add(job["job_type"])
    return unique_job_titles


def filter_by_job_type(jobs, job_type):
    jobs_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_list.append(job)
    return jobs_list


def get_unique_industries(path):
    all_jobs = read(path)
    unique_industries = set()
    for job in all_jobs:
        if len(job["industry"]) > 0:
            unique_industries.add(job["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    jobs_list = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_list.append(job)
    return jobs_list


def get_max_salary(path):
    all_jobs = read(path)
    all_jobs_filter = set()
    for job in all_jobs:
        if job["max_salary"]:
            try:
                all_jobs_filter.add(int(job["max_salary"]))
            except ValueError:
                continue
    return max(all_jobs_filter)

    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    pass


def get_min_salary(path):
    all_jobs = read(path)
    all_jobs_filter = set()
    for job in all_jobs:
        if job["min_salary"]:
            try:
                all_jobs_filter.add(int(job["min_salary"]))
            except ValueError:
                continue
    return min(all_jobs_filter)
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    pass


def matches_salary_range(job, salary):
    """
    if job["min_salary"] < salary < job["max_salary"]:
        return True
    elif salary < job["min_salary"] or salary > job["max_salary"]:
        return False
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("A very specific bad thing happened.")
    elif type(job["min_salary"]) and type(job["max_salary"]) != int:
        raise ValueError("A very specific bad thing happened.")
    elif type(salary) != int:
        raise ValueError("A very specific bad thing happened.")
    elif job["min_salary"] or job["max_salary"] is None:
        raise ValueError("A very specific bad thing happened.")
    """


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

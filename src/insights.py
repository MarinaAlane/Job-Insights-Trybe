from src import jobs


def get_unique_job_types(path):
    job_types = []
    for job in jobs.read(path):
        job_types.append(job["job_type"])
    return list(set(job_types))


def filter_by_job_type(jobs, job_type):
    """
    references:
    https://www.pythontutorial.net/python-basics/python-filter-list/"""
    job_by_type = list(filter(lambda job: job["job_type"] == job_type, jobs))
    return job_by_type


def get_unique_industries(path):
    industries = []
    for job in jobs.read(path):
        if job["industry"] == "" or job["industry"] in industries:
            pass
        else:
            industries.append(job["industry"])
    return list(set(industries))


def filter_by_industry(jobs, industry):
    ind_by_job = filter(lambda job: job["industry"] == industry, jobs)
    return list(ind_by_job)


def get_max_salary(path):
    biggest_salary = 0
    for job in jobs.read(path):
        if job["max_salary"] == "" or not job["max_salary"].isdigit():
            continue
        elif int(job["max_salary"]) > biggest_salary:
            biggest_salary = int(job["max_salary"])
    return biggest_salary


def get_min_salary(path):
    smallest_salary = get_max_salary(path)
    for job in jobs.read(path):
        if job["min_salary"] == "" or not job["min_salary"].isdigit():
            continue
        elif int(job["min_salary"]) < smallest_salary:
            smallest_salary = int(job["min_salary"])
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

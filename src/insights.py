from .jobs import read


def get_unique_job_types(path):
    listJobs = read(path)
    setJobs = set()
    for job in listJobs:
        setJobs.add(job["job_type"])
    return setJobs


def filter_by_job_type(jobs, job_type):
    return [j for j in jobs if j["job_type"] == job_type]


def get_unique_industries(path):
    listJobs = read(path)
    setJobs = set()
    for job in listJobs:
        if "industry" in job:
            if job["industry"] != "":
                setJobs.add(job["industry"])
    return setJobs


def filter_by_industry(jobs, industry):
    return [j for j in jobs if j["industry"] == industry]


def get_max_salary(path):
    listJobs = read(path)
    value = 0
    for job in listJobs:
        if job["max_salary"] != "" and job["max_salary"].isnumeric():
            if int(job["max_salary"]) > value:
                value = int(job["max_salary"])
    return value


def get_min_salary(path):
    listJobs = read(path)
    value = get_max_salary(path)
    for job in listJobs:
        if job["min_salary"] != "" and job:
            if int(job["min_salary"]) < value:
                value = int(job["min_salary"])
    return value


# print(get_min_salary("src/jobs.csv"))


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

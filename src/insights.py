from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    job_types = set()

    for job in jobs_list:
        job_types.add(job["job_type"])

    return list(job_types)


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    jobs_list = read(path)
    industry_types = set()

    for job in jobs_list:
        if job["industry"] != "":
            industry_types.add(job["industry"])

    return list(industry_types)


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
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = set()

    for job in jobs_list:
        # Source: www.programiz.com/python-programming/methods/string/isnumeric
        if job["max_salary"].isnumeric():
            max_salary.add(int(job["max_salary"]))

    return max(max_salary)


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = set()

    for job in jobs_list:
        if job["min_salary"].isnumeric():
            min_salary.add(int(job["min_salary"]))

    return min(min_salary)


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
        True if the salary is in the salary range of the job,
        False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if "min_salary" not in job:
        raise ValueError
    if "max_salary" not in job:
        raise ValueError
    if not isinstance(job["min_salary"], int):
        raise ValueError
    if not isinstance(job["max_salary"], int):
        raise ValueError
    if not isinstance(salary, int):
        raise ValueError
    if job["min_salary"] > job["max_salary"]:
        raise ValueError

    return job["min_salary"] <= salary <= job["max_salary"]

# Comments: Ajuda do Rahel Martim no plantão do dia 25/12/2022 as 13:40
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
    salary_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salary_range.append(job)
        except ValueError:
            pass
    return salary_range

from src.jobs import read


def get_unique_job_types(path):
    csvList = read(path)
    job_types = set()
    for item in csvList:
        for job in item["job_type"].split(","):
            job_types.add(job)
    return job_types


def filter_by_job_type(jobs, job_type):
    job_type_list = []
    for job in jobs:
        if job['job_type'] == job_type:
            job_type_list.append(job)
    return job_type_list


def get_unique_industries(path):
    arr_csv = read(path)
    uniqueIndustriesList = set()
    for item in arr_csv:
        industry = item["industry"]
        if (industry != ''):
            uniqueIndustriesList.add(industry)
    return uniqueIndustriesList


def filter_by_industry(jobs, industry):
    filter_industry = []
    for job in jobs:
        if job['industry'] == industry:
            filter_industry.append(job)
    return filter_industry


def get_max_salary(path):
    arr_csv = read(path)
    max_salaries = []
    for item in arr_csv:
        if (item['max_salary'] != '' and item['max_salary'] != 'invalid'):
            max_salaries.append(int(item['max_salary']))
    max_salaries.sort()
    return max_salaries[-1]


def get_min_salary(path):
    arr_csv = read(path)
    min_salaries = []
    for item in arr_csv:
        if (item['min_salary'] != '' and item['min_salary'] != 'invalid'):
            min_salaries.append(int(item['min_salary']))
    min_salaries.sort()
    return min_salaries[0]


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

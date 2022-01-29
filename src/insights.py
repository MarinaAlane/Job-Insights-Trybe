from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    # dict_of_unique_jobs = {}
    array_of_types = set()
    for job_type in jobs:
        array_of_types.add(job_type["job_type"])
    return list(array_of_types)


def filter_by_job_type(jobs, job_type):
    filtered_job = filter(lambda job: (job["job_type"] == job_type), jobs)
    return list(filtered_job)


def remove_empty(array):
    for item in array:
        if item != "":
            return True
        else:
            return False


def get_unique_industries(path):
    industries = read(path)
    # dict_of_unique_jobs = {}
    array_of_industries = set()
    for industry in industries:
        array_of_industries.add(industry["industry"])
    # método encontrado em
    # https://www.programiz.com/python-programming/methods/built-in/filter
    filtered_industries = filter(remove_empty, array_of_industries)
    return list(filtered_industries)


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
    return []


def get_max_salary(path):
    document = read(path)
    array_of_salaries = set()
    for item in document:
        try:
            array_of_salaries.add(int(item["max_salary"]))
        except ValueError:
            pass

    return max(array_of_salaries)


def get_min_salary(path):
    document = read(path)
    array_of_salaries = set()
    for item in document:
        try:
            array_of_salaries.add(int(item["min_salary"]))
        except ValueError:
            pass

    return min(array_of_salaries)


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

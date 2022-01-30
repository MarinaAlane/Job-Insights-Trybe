from src.jobs import read


def get_unique_job_types(path):
    csv_data = read(path)

    job_types = set()
    job_types_list = []

    for job in csv_data:
        job_types.add(job['job_type'])

    for job_type in job_types:
        job_types_list.append(job_type)

    return job_types_list


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
    return []


def get_unique_industries(path):
    csv_data = read(path)

    industries = set()
    industries_list = []

    for industry in csv_data:
        industries.add(industry['industry'])

    for industry in industries:
        industries_list.append(industry)

    return list(filter(None, industries_list))


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
    csv_data = read(path)

    salaries_not_formatted = []
    salary_numbered_list = []

    for salary in csv_data:
        salaries_not_formatted.append(salary['max_salary'])

    salary_formatted = list(filter(None, salaries_not_formatted))

    for salary in salary_formatted:
        salary_numbered_list.append(int(salary))

    return (max(salary_numbered_list))


def get_min_salary(path):
    csv_data = read(path)

    salaries_not_formatted = []
    salary_numbered_list = []

    for salary in csv_data:
        salaries_not_formatted.append(salary['min_salary'])

    salary_formatted = list(filter(None, salaries_not_formatted))

    for salary in salary_formatted:
        salary_numbered_list.append(int(salary))

    return (min(salary_numbered_list))


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

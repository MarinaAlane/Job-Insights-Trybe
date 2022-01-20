from src.jobs import read


def get_unique_job_types(path):
    result = set()
    for row in read(path):
        result.add(row["job_type"])
    return result


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
    result = set()
    for row in read(path):
        industry = row["industry"]
        if not industry.strip() == '':
            result.add(row["industry"].strip())
    return result


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
    biggest_salary = 0
    for row in read(path):
        salary = row["max_salary"]
        if not salary.strip() == '':
            if not salary == 'invalid':
                if int(salary) > int(biggest_salary):
                    biggest_salary = salary
    print(biggest_salary)
    return int(biggest_salary)


def get_min_salary(path):
    data = read(path)
    current = 0
    min_salary = data[current]["min_salary"]

    while min_salary == '' or min_salary == 'invalid':
        current = current + 1
        min_salary = data[current]["min_salary"]

    for row in data:
        current_salary = row["min_salary"]
        if not current_salary.strip() == '':
            if not current_salary == 'invalid':
                if int(current_salary) < int(min_salary):
                    min_salary = current_salary
    return int(min_salary)


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

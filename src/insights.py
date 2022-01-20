from src.jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)
    job_types = set()
    for item in all_jobs:
        for job in item['job_type'].split(','):
            job_types.add(job)
    return job_types
    # job_types = {}
    # for item in jobs:
    #     for job in item['job_type'].split(','):
    #         if job in job_types:
    #             job_types[job]['jobs'] += 1
    #         else:
    #             job_types[job] = {'jobs': 1}


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job['job_type'] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    all_jobs = read(path)
    industry = set()
    for item in all_jobs:
        job = item['industry']
        if job != '':
            industry.add(item['industry'])
    return industry


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
    all_jobs = read(path)
    max_salary = int(0)
    for salary in all_jobs:
        curr_salary = salary['max_salary']
        if curr_salary != '' and curr_salary != 'invalid':
            int_curr_salary = int(curr_salary)
            if (int_curr_salary > max_salary):
                max_salary = int_curr_salary
    return max_salary


def get_min_salary(path):
    all_jobs = read(path)
    min_salary = 0
    for salary in all_jobs:
        curr_salary = salary['min_salary']
        if curr_salary != '' and curr_salary != 'invalid':
            if min_salary == 0:
                min_salary = int(curr_salary)
            int_curr_salary = int(curr_salary)
            if (int_curr_salary < min_salary):
                min_salary = int_curr_salary
    return min_salary


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

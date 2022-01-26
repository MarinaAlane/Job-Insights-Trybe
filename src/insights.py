from src.jobs import read


def get_unique_job_types(path):  # ok
    all_jobs_list = read(path)
    unique_job = set()

    for job in all_jobs_list:
        if job['job_type'] is not None:
            unique_job.add(job['job_type'])
    return unique_job


def filter_by_job_type(jobs, job_type):  # ok
    job_list = [job for job in jobs if job['job_type'] == job_type]
    return job_list


def get_unique_industries(path):  # ok
    all_jobs_list = read(path)
    industry_values = set()

    for job in all_jobs_list:
        if job['industry'] != '':
            industry_values.add(job['industry'])
    return industry_values


def filter_by_industry(jobs, industry):
    job_list = [job for job in jobs if job['industry'] == industry]
    return job_list


def get_max_salary(path):  # ok
    all_jobs_list = read(path)
    all_salaries = set()

    for job in all_jobs_list:
        if job['max_salary'] != '' and job['max_salary'] != 'invalid':
            all_salaries.add(int(job['max_salary']))
    result = sorted(all_salaries)[-1]
    return result


def get_min_salary(path):  # ok
    all_jobs_list = read(path)
    all_salaries = set()

    for job in all_jobs_list:
        if job['min_salary'] != '' and job['min_salary'] != 'invalid':
            all_salaries.add(int(job['min_salary']))
    result = sorted(all_salaries)[0]
    return result


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

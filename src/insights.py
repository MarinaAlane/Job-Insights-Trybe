from src import jobs

# import jobs


def get_unique_job_types(path):
    jobs_list = jobs.read(path)
    job_types = list()
    for job in jobs_list:
        if job["job_type"] in job_types:
            pass
        else:
            job_types.append(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    jobs_by_job_type = list()
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_by_job_type.append(job)
        else:
            continue
    return jobs_by_job_type


def get_unique_industries(path):
    jobs_list = jobs.read(path)
    job_industries = list()
    for job in jobs_list:
        if job["industry"] == "" or job["industry"] in job_industries:
            pass
        else:
            job_industries.append(job["industry"])
    return job_industries


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
    job_list = jobs.read(path)
    highest_salary = 0
    for job in job_list:
        if job["max_salary"] == "" or not job["max_salary"].isnumeric():
            continue
        elif int(job["max_salary"]) > highest_salary:
            highest_salary = int(job["max_salary"])
    return highest_salary


def get_min_salary(path):
    job_list = jobs.read(path)
    lowest_salary = 0
    for job in job_list:
        if job["min_salary"] == "" or not job["min_salary"].isnumeric():
            continue
        elif lowest_salary == 0 or int(job["min_salary"]) < lowest_salary:
            lowest_salary = int(job["min_salary"])
    return lowest_salary


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

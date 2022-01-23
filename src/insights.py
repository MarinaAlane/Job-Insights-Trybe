from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    unique_jobs = set()
    for type in jobs_list:
        unique_jobs.add(type["job_type"])

    return unique_jobs

    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """


def filter_by_job_type(jobs, job_type):
    # print(jobs)
    # print("Dicionario Tipos de Jobs" + job_type)
    job_type = [job for job in jobs if job_type in job.values()]
    # print(job_type)
    return job_type
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


def get_unique_industries(path):
    industry_list = read(path)
    unique_industries = [industry["industry"] for industry in industry_list if
                         industry["industry"] != ""]
    # print(set(unique_industries))
    return set(unique_industries)
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """


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


# https://www.delftstack.com/pt/howto/python/convert-string-to-int-in-python/
# - converter strint em inteiro
def get_max_salary(path):
    all_salaries = read(path)
    max_salary = [salary["max_salary"] for salary in all_salaries
                  if salary["max_salary"].isnumeric()
                  if salary["max_salary"] != ""]
    max_salary_int = [int(int_salary) for int_salary in max_salary]
    # max_salary_int = int(max_salary)
    print(max(max_salary_int))
    return (max(max_salary_int))
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """


def get_min_salary(path):
    all_salaries = read(path)
    min_salary = [salary["min_salary"] for salary in all_salaries
                  if salary["min_salary"].isnumeric()
                  if salary["min_salary"] != ""]
    min_salary_int = [int(int_salary) for int_salary in min_salary]
    # max_salary_int = int(max_salary)
    print(min(min_salary_int))
    return (min(min_salary_int))
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """


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

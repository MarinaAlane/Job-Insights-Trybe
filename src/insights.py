from src.jobs import read
# from src.jobs import read
# from src import jobs
# import jobs


# chamar a lista csv
# criar a variavel da lista, só que vazia
# fazer o laço para a lista se não tiver o tipo job type acrescente a lista
# retorna tudo isso


def get_unique_job_types(path):
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
    list_dict = read(path)
    jobs_filter = []
    for job in list_dict:
        if not job["job_type"] in jobs_filter:
            jobs_filter.append(job["job_type"])
    return jobs_filter


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
    jobs_filter = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filter.append(job)
    return jobs_filter


def get_unique_industries(path):
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
    list_dict = read(path)
    ind_filter = []
    for ind in list_dict:
        if not ind["industry"] in ind_filter and ind["industry"] != "":
            ind_filter.append(ind["industry"])
    return ind_filter


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
    job_filter_by_ind = []
    for job in jobs:
        if job["industry"] == industry:
            job_filter_by_ind.append(job)
    return job_filter_by_ind


def get_max_salary(path):
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
    list_dict = read(path)
    salary_max = 0
    salary_list = []
    for salary in list_dict:
        if salary["max_salary"].isdigit():
            salary_list.append(int(salary["max_salary"]))

    for salary in salary_list:
        if salary > salary_max:
            salary_max = salary
    return salary_max


def get_min_salary(path):
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
    list_dict = read(path)
    salary_min = 100000
    salary_list = []
    for salary in list_dict:
        if salary["min_salary"].isdigit():
            salary_list.append(int(salary["min_salary"]))
    for salary in salary_list:
        if salary < salary_min:
            salary_min = salary
    return salary_min


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
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("not found")

    elif salary is None:
        raise ValueError("not found")

    elif not isinstance(job["min_salary"], int) or not isinstance(
        job["max_salary"], int
    ):
        raise ValueError("not integer")

    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("value does not make sense")

    else:
        return job["min_salary"] <= salary <= job["max_salary"]


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
    filtered_salary_range = []
    for job in jobs:
        if (
            isinstance(salary, int)
            and isinstance(job["min_salary"], int)
            and isinstance(job["max_salary"], int)
        ):
            if job["min_salary"] <= salary <= job["max_salary"]:
                filtered_salary_range.append(job)
    return filtered_salary_range

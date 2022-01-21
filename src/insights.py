from src.jobs import read

# from jobs import read


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
    jobs_list = read(path)
    job_set = {job["job_type"] for job in jobs_list}

    return [*job_set]


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
    filtered_jobs = filter(lambda type: type["job_type"] == job_type, jobs)

    return [*filtered_jobs]


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
    jobs_list = read(path)
    job_set = {job["industry"] for job in jobs_list}
    filter_falsy_values = filter(lambda i: i, job_set)

    return [*filter_falsy_values]


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
    filtered_jobs = filter(lambda type: type["industry"] == industry, jobs)

    return [*filtered_jobs]


def cast_valid_values(string):
    try:
        return int(string)
    except ValueError:
        return 0


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
    jobs_list = read(path)
    job_max_salary_list = [
        cast_valid_values(job["max_salary"]) for job in jobs_list
    ]

    return max(job_max_salary_list)


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
    jobs_list = read(path)
    job_min_salary_list = {
        cast_valid_values(job["min_salary"]) or None for job in jobs_list
    }
    remove_zeros = filter(
        lambda value: value not in [0, None], job_min_salary_list
    )

    return min(remove_zeros)


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
    try:
        max_salary = job["max_salary"]
        min_salary = job["min_salary"]
        arg_types = [max_salary, min_salary, salary]

        if not all([isinstance(el, int) for el in arg_types]):
            raise ValueError("All args must be ints")

        if min_salary > max_salary:
            raise ValueError("min_salary can not be higher than max_salary")

        return min_salary <= salary <= max_salary
    except KeyError:
        raise ValueError("keys min_salary or max_salary are missing in job;")


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

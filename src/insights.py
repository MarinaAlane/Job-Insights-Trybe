from src.jobs import read

# import pprint


def get_unique_job_types(path):
    data_jobs = read(path)
    unique_job_types = list({job["job_type"] for job in data_jobs})
    return unique_job_types


def filter_by_job_type(jobs, job_type):
    filtered_job_type = [job for job in jobs if job["job_type"] == job_type]
    return filtered_job_type


def get_unique_industries(path):
    data_jobs = read(path)
    unique_industries = list(
        {job["industry"] for job in data_jobs if len(job["industry"]) > 0}
    )
    return unique_industries


def filter_by_industry(jobs, industry):
    filtered_industry = [job for job in jobs if job["industry"] == industry]
    return filtered_industry


def get_max_salary(path):
    data_jobs = read(path)
    max_salary = max(
        [
            int(job["max_salary"])
            for job in data_jobs
            if job["max_salary"].isnumeric() is True
        ]
    )
    return max_salary


def get_min_salary(path):
    data_jobs = read(path)
    min_salary = min(
        [
            int(job["min_salary"])
            for job in data_jobs
            if job["min_salary"].isnumeric() is True
        ]
    )
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


# https://learncodeimprove.com/python/list-of-unique-items-comprehension/
# https://www.w3schools.com/python/ref_string_isnumeric.asp

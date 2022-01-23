# from jobs import read
from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    job_types_set = set()
    [job_types_set.add(job["job_type"]) for job in jobs_list]
    job_types_list = list(job_types_set)
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
    job_with_same_job_type = [
        job for job in jobs if job["job_type"] == job_type
    ]
    return job_with_same_job_type


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
    unique_industries_set = set()
    [
        unique_industries_set.add(job["industry"])
        for job in jobs_list
        if job["industry"]
    ]
    unique_industries_list = list(unique_industries_set)
    return unique_industries_list


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
    job_by_industy = [job for job in jobs if job["industry"] == industry]
    return job_by_industy


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
    max_salary = 0
    for job in jobs_list:
        if job["max_salary"] and job["max_salary"].isnumeric():
            if int(job["max_salary"]) > max_salary:
                max_salary = int(job["max_salary"])
    return max_salary


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
    min_salary = get_max_salary(path)
    for job in jobs_list:
        if job["min_salary"] and job["min_salary"].isnumeric():
            if int(job["min_salary"]) < min_salary:
                min_salary = int(job["min_salary"])
    return min_salary


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError()

    if type(job["max_salary"]) != int or type(job["min_salary"]) != int:
        raise ValueError()

    if type(salary) != int:
        raise ValueError()

    if job["min_salary"] > job["max_salary"]:
        raise ValueError()

    return salary >= job["min_salary"] and salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    jobs_in_range_list = list()
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_in_range_list.append(job)
        except ValueError:
            continue

    return list(jobs_in_range_list)

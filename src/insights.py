from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them
    """
    jobs = read(path)

    unique_jobs_type = set()

    for job in jobs:
        for job_type in job["job_type"].split(","):
            unique_jobs_type.add(job_type)

    return unique_jobs_type


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type
    """

    jobs_found = []

    for job in jobs:

        if job["job_type"] == job_type:
            jobs_found.append(job)

    return jobs_found


def get_unique_industries(path):
    """Checks all different industries and returns a list of them
    """

    jobs = read(path)

    industries = set()

    for job in jobs:
        industry = job["industry"]
        if (industry != ""):
            industries.add(industry)

    return industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industr
    """

    jobs_found = []

    for job in jobs:

        if job["industry"] == industry:
            jobs_found.append(job)

    return jobs_found


def get_max_salary(path):
    """Get the maximum salary of all jobs
    """

    jobs = read(path)

    highest_maximum_salary = 0

    for job in jobs:
        try:
            max_salary = int(job["max_salary"])
            if max_salary and max_salary > highest_maximum_salary:
                highest_maximum_salary = max_salary
        except ValueError:
            pass

    return highest_maximum_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs
    """

    jobs = read(path)

    lower_salary = 90000

    for job in jobs:
        try:
            min_salary = int(job["min_salary"])
            if min_salary and min_salary < lower_salary:
                lower_salary = min_salary
        except ValueError:
            pass

    return lower_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job
    """
    if (
        "min_salary" not in job or
        "max_salary" not in job or
        type(job["min_salary"]) != int or
        type(job["max_salary"]) != int or
        job["min_salary"] > job["max_salary"] or
        type(salary) != int
    ):
        raise ValueError("Error")
    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


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

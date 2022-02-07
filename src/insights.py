from src import jobs


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
    all_jobs = jobs.read(path)

    types_jobs = set()

    for job in all_jobs:
        types_jobs.add(job["job_type"])

    return types_jobs


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
    return [job for job in jobs if job["job_type"] == job_type]


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
    all_jobs = jobs.read(path)

    industries = set()

    for job in all_jobs:
        if job["industry"]:
            industries.add(job["industry"])

    return industries


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
    return [job for job in jobs if job["industry"] == industry]


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
    all_jobs = jobs.read(path)

    max_salary = 0

    for job in all_jobs:
        if job["max_salary"].isdigit():
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
    all_jobs = jobs.read(path)

    min_salary = min(
        [
            int(job["min_salary"])
            for job in all_jobs
            if job["min_salary"].isnumeric()
        ]
    )

    return min_salary


def has_salary_data(job):
    if "min_salary" in job and "max_salary" in job:
        return True
    return False


def has_correct_salary_type(job):
    if isinstance(job["min_salary"], int) and isinstance(
        job["max_salary"], int
    ):
        return True
    return False


def min_less_than_max(job):
    if job["min_salary"] > job["max_salary"]:
        return False
    return True


def salary_between_range(job, salary):

    if not isinstance(salary, int):
        return False

    min, max = job["min_salary"], job["max_salary"]

    return (
        has_salary_data(job)
        and has_correct_salary_type(job)
        and min <= salary <= max
    )


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
        raise (ValueError())

    min_salary, max_salary = job["min_salary"], job["max_salary"]

    if not isinstance(min_salary, int) or not isinstance(max_salary, int):
        raise (ValueError())

    if min_salary > max_salary:
        raise (ValueError())

    if not isinstance(salary, int):
        raise (ValueError())

    return min_salary <= salary <= max_salary


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
    filtered_jobs_by_salary_range = [
        job
        for job in jobs
        if has_salary_data(job)
        and has_correct_salary_type(job)
        and min_less_than_max(job)
        and salary_between_range(job, salary)
    ]

    return filtered_jobs_by_salary_range

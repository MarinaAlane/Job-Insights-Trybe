from src import jobs


def get_unique_job_types(path):

    data = jobs.read(path)

    unique_jobs = set()

    for job in data:
        unique_jobs.add(job["job_type"])

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
    return list(unique_jobs)


def filter_by_job_type(jobs, job_type):

    filtered_jobs_by_job_type = [
        job for job in jobs if job["job_type"] == job_type
    ]

    """Filters a list of jobs by job_type

    [
        industry for industry in list(unique_industries) if industry != ""
    ]

    [
            int(job["min_salary"])
            for job in data
            if job["min_salary"].isnumeric()
        ]

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
    return filtered_jobs_by_job_type


def get_unique_industries(path):

    data = jobs.read(path)

    unique_industries = set()

    for job in data:
        unique_industries.add(job["industry"])

    unique_industires_without_empty_value = [
        industry for industry in list(unique_industries) if industry != ""
    ]

    """
    https://note.nkmk.me/en/python-list-clear-pop-remove-del/

    Checks all different industries and returns a list of them

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
    return unique_industires_without_empty_value


def filter_by_industry(jobs, industry):

    filtered_jobs_by_industry = [
        job for job in jobs if job["industry"] == industry
    ]
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
    return filtered_jobs_by_industry


def get_max_salary(path):

    data = jobs.read(path)

    max_salary = 0

    for job in data:
        if job["max_salary"].isdigit():
            if int(job["max_salary"]) > max_salary:
                max_salary = int(job["max_salary"])

    return max_salary

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

    data = jobs.read(path)

    min_salary = min(
        [
            int(job["min_salary"])
            for job in data
            if job["min_salary"].isnumeric()
        ]
    )

    return min_salary
    """
    https://stackoverflow.com/questions/5320871/how-to-find-the-min-max-value-of-a-common-key-in-a-list-of-dicts

    Get the minimum salary of all jobs

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

    if "min_salary" not in job or "max_salary" not in job:
        raise (ValueError())

    min_salary, max_salary = job["min_salary"], job["max_salary"]

    if not isinstance(min_salary, int) or not isinstance(max_salary, int):
        raise (ValueError())

    if min_salary > max_salary:
        raise (ValueError())

    if not isinstance(salary, int):
        raise (ValueError())
    """
    https://www.kite.com/python/answers/how-to-check-if-a-number-is-an-integer-in-python

    Checks if a given salary is in the salary range of a given job

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
    return min_salary <= salary <= max_salary


def filter_by_salary_range(jobs, salary):

    filtered_jobs_by_salary_range = [
        job
        for job in jobs
        if has_salary_data(job)
        and has_correct_salary_type(job)
        and min_less_than_max(job)
        and salary_between_range(job, salary)
    ]
    """
    Filters a list of jobs by salary range

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
    return filtered_jobs_by_salary_range

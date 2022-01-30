from src.jobs import read


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
    jobs_read = read(path)
    jobs_list = {job["job_type"] for job in jobs_read}

    return list(jobs_list)


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
    selected_jobs = [job for job in jobs if job["job_type"] == job_type]
    return selected_jobs


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
    jobs_read = read(path)
    industries_list = {
        industries["industry"]
        for industries in jobs_read
        if not industries["industry"] == ""
    }
    return list(industries_list)


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
    selected_industries = [ind for ind in jobs if ind["industry"] == industry]
    return selected_industries


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
    jobs_read = read(path)
    salary_max = [
        int(salary["max_salary"])
        for salary in jobs_read
        if salary["max_salary"].isdigit()
    ]
    return max(salary_max)


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
    jobs_read = read(path)
    salary_min = [
        int(salary["min_salary"])
        for salary in jobs_read
        if salary["min_salary"].isdigit()
    ]
    return min(salary_min)


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
    for value in job:
        if "min_salary" and "max_salary" not in job:
            raise ValueError()
        elif type(job[value]) != int:
            raise ValueError()
    if job["min_salary"] > job["max_salary"] or type(salary) != int:
        raise ValueError()
    return salary >= job["min_salary"] and salary <= job["max_salary"]


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
    list_valid_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_valid_jobs.append(job)
        except ValueError:
            print('Deu errado!')
    return list_valid_jobs

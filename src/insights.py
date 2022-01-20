import src.jobs


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
    jobs_dicts_list = src.jobs.read(path)

    job_types = {job["job_type"] for job in jobs_dicts_list}

    return [job_type for job_type in job_types]


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
    jobs_meeting_type = [job for job in jobs if job["job_type"] == job_type]
    return jobs_meeting_type


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
    jobs_dicts_list = src.jobs.read(path)

    industries_set = {
        job["industry"] for job in jobs_dicts_list if job["industry"] != ""
    }

    return [industry for industry in industries_set]


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
    jobs_meeting_industy = [job for job in jobs if job["industry"] == industry]
    return jobs_meeting_industy


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
    jobs_dicts_list = src.jobs.read(path)

    salaries_set = {
        job["max_salary"] for job in jobs_dicts_list if job["max_salary"] != ""
    }

    salaries_list = [
        int(salary) for salary in salaries_set if salary.isdigit()
    ]

    salaries_list.sort()

    biggest_salary = salaries_list[-1]

    return biggest_salary


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
    jobs_dicts_list = src.jobs.read(path)

    salaries_set = {
        job["min_salary"] for job in jobs_dicts_list if job["min_salary"] != ""
    }

    salaries_list = [
        int(salary) for salary in salaries_set if salary.isdigit()
    ]

    salaries_list.sort()

    min_salary = salaries_list[0]

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
    if len(job) < 2:
        raise ValueError

    min_salary, max_salary = job["min_salary"], job["max_salary"]

    if min_salary is None or max_salary is None:
        raise ValueError
    elif type(min_salary) != int or type(max_salary) != int:
        raise ValueError
    elif min_salary > max_salary:
        raise ValueError

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
    rigth_jobs = []
    for i in range(len(jobs)):
        if not type(salary) == int:
            break
        try:
            if matches_salary_range(jobs[i], salary) and type(salary) == int:
                rigth_jobs.append(jobs[i])
        except ValueError:
            pass
    return rigth_jobs

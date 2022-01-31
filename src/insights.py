import src.jobs as jobs


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
    jobs_ = jobs.read(path)
    job_type = {job["job_type"] for job in jobs_}
    return job_type


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
    jobs_ = jobs.read(path)
    industries = {job["industry"] for job in jobs_ if job["industry"] != ""}
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


def get_salaries(jobs, type_):
    """Get all salaries jobs

    Parameters
    ----------
    jobs: list[dict[str,str]]
        It can be from read

    Returns
    -------
    list[int]
        List of all salaries paid out

    """
    amount_type = f"{type_}_salary"
    salaries = []
    for job in jobs:
        if job[amount_type] != "" and job[amount_type].isdigit():
            salary = int(job[amount_type])
            salaries.append(salary)
    return salaries


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
    jobs_ = jobs.read(path)
    salaries = get_salaries(jobs_, "max")
    return max(salaries)


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
    jobs_ = jobs.read(path)
    salaries = get_salaries(jobs_, "min")
    return min(salaries)


def is_integer(n):
    """Check if a number is integer

    Parameters
    ----------
    n : int

    Returns
    -------
    bool
        True if n is interger. False otherwise
    """
    try:
        float(n)
    except (ValueError, TypeError):
        return False
    else:
        return float(n).is_integer()


def check_args_salary_range(job, salary):
    if not (
            str(job["max_salary"]).isdigit()
            and str(job["min_salary"]).isdigit()
    ):
        return False
    else:
        if not (
            is_integer(job["min_salary"])
            and is_integer(job["max_salary"])
            and is_integer(salary)
        ):
            return False
        else:
            min_salary = job["min_salary"]
            max_salary = job["max_salary"]
            if min_salary > max_salary:
                return False
            else:
                return True


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
        if check_args_salary_range(job, salary):
            min_salary = int(job["min_salary"])
            max_salary = int(job["max_salary"])
            if min_salary <= int(salary) <= max_salary:
                return True
            else:
                return False
        else:
            raise ValueError()
    except (ValueError, KeyError):
        raise ValueError()


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
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass
    return filtered_jobs

from .jobs import read


def get_unique_job_types(path):
    data = read(path)
    job_type = {job["job_type"] for job in data}
    return job_type
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
    return []


def filter_by_job_type(jobs, job_type):
    filter = [job for job in jobs if job["job_type"] == job_type]
    return filter
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
    return []


def get_unique_industries(path):
    data = read(path)
    single_industry = set()
    for industry in data:
        if industry["industry"] != "":
            single_industry.add(industry["industry"])
    return single_industry
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
    return []


def filter_by_industry(jobs, industry):
    filter = [job for job in jobs if job["industry"] == industry]
    return filter
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
    return []


def get_max_salary(path):
    data = read(path)
    max_sal = []
    for salary in data:
        # Verifique se todos os caracteres no texto são numéricos:
        # Tive dica do Antônio Schappo com isnumeric
        if salary["max_salary"].isnumeric():
            number = int(salary["max_salary"])
            max_sal.append(number)
    return max(max_sal)

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
    pass


def get_min_salary(path):
    data = read(path)
    min_sal = []
    for salary in data:
        # Verifique se todos os caracteres no texto são numéricos:
        if salary["min_salary"].isnumeric():
            number = int(salary["min_salary"])
            min_sal.append(number)
    return min(min_sal)
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
    pass


def matches_salary_range(job, salary):
    # https://www.w3schools.com/python/ref_keyword_raise.asp
    # alguma das chaves min_salary ou max_salary estão ausentes no dicionário;
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    # alguma das chaves min_salary ou max_salary tem valores não-numéricos;
    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError
    # o valor de min_salary é maior que o valor de max_salary;
    if job["min_salary"] > job["max_salary"]:
        raise ValueError
    # o parâmetro salary tem valores não-numéricos;
    if type(salary) != int:
        raise ValueError

    is_salary_range = job["min_salary"] <= salary <= job["max_salary"]
    return is_salary_range
    # https://stackoverflow.com/questions/13628791/determine-whether-integer-is-between-two-other-integers

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

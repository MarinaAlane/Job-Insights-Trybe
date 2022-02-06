from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_Types = set()
    for job in jobs:
        job_Types.add(job["job_type"])
    return job_Types


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
    Alljobs = list()

    for job in jobs:
        if (job["job_type"] == job_type):
            Alljobs.append(job)
    return Alljobs


def get_unique_industries(path):
    industries = read(path)
    industry_Types = set()
    for industry in industries:
        if (industry["industry"]):
            industry_Types.add(industry["industry"])
    return industry_Types


def filter_by_industry(jobs, industry):
    industries = list()

    for job in jobs:
        if (job["industry"] == industry):
            industries.append(job)
    return industries
    

def get_max_salary(path):
    jobs = read(path)
    salaries_maximum = [
        int(salary["max_salary"])
        # convertendo o que vier (string ou float) para inteiro
        for salary in jobs
        if salary["max_salary"] != ""
        and salary["max_salary"].isnumeric()
    ]
    return max(salaries_maximum)


def get_min_salary(path):
    jobs = read(path)
    salaries_minimum = [
        int(salary["min_salary"])   
        # convertendo o que vier (string ou float) para inteiro
        for salary in jobs
        if salary["min_salary"] != ""
        and salary["min_salary"].isnumeric()
    ]
    return min(salaries_minimum)

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

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
    if(
        type(job["min_salary"]) != int or
        type(job["max_salary"]) != int or
        type(salary) != int or
        job["min_salary"] > job["max_salary"]
    ):
        raise ValueError
        return job["min_salary"] <= salary <= job["max_salary"]


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

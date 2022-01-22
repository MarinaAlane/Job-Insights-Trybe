from src.jobs import read


def get_unique_job_types(path):
    jobs_types = set()
    jobs_dict = read(path)

    for job in jobs_dict:
        jobs_types.add(job["job_type"])

    return list(jobs_types)


def filter_by_job_type(jobs, job_type):
    job_type_list = []

    for job in jobs:
        if job["job_type"] == job_type:
            job_type_list.append(job)

    return job_type_list


def get_unique_industries(path):
    job_industries = set()
    jobs_dict = read(path)

    for job in jobs_dict:
        if job["industry"] != "":
            job_industries.add(job["industry"])

    return list(job_industries)


def filter_by_industry(jobs, industry):
    job_industry_list = []

    for job in jobs:
        if job["industry"] == industry:
            job_industry_list.append(job)

    return job_industry_list


def get_max_salary(path):
    max_salaries = set()
    jobs_dict = read(path)

    for job in jobs_dict:
        if job["max_salary"].isnumeric():
            max_salaries.add(int(job["max_salary"]))

    return max(list(max_salaries))


def get_min_salary(path):
    min_salaries = set()
    jobs_dict = read(path)

    for job in jobs_dict:
        if job["min_salary"].isnumeric():
            min_salaries.add(int(job["min_salary"]))

    return min(list(min_salaries))


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("`job` must have `min_salary` and `max_salary` keys")

    elif (type(job["min_salary"]) == str or type(job["max_salary"]) == str or
          type(salary) != int):
        raise ValueError("`job` must have `min_salary` and `max_salary` as")

    elif job["max_salary"] < job["min_salary"]:
        raise ValueError("`job` must have `min_salary` less than `max_salary`")

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

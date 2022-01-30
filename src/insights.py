from src.jobs import read


def get_unique_job_types(path):
    result = read(path)
    job_type = set()
    for job in result:
        job_type.add(job["job_type"])
    return job_type


def filter_by_job_type(jobs, job_type):
    jobs_filtered = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filtered.append(job)
    return jobs_filtered


def get_unique_industries(path):
    result = read(path)
    industries = set()
    for job in result:
        industries.add(job["industry"])
    result_list = list(industries)
    list_without_empty = []
    for indusrty in result_list:
        if indusrty != "":
            list_without_empty.append(indusrty)
    return list_without_empty


def filter_by_industry(jobs, industry):
    jobs_filtered = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_filtered.append(job)
    return jobs_filtered


def get_max_salary(path):
    result = read(path)
    salary = set()
    for job in result:
        try:
            salary.add(int(job["max_salary"]))
        except ValueError:
            pass
    # salary_array = list(salary)
    # salary_without_empty = []
    # for salary in salary_array:
    #     if salary != "":
    #         salary_without_empty.append(int(salary))
    max_salary = max(salary)
    return max_salary


def get_min_salary(path):
    result = read(path)
    salary = set()
    for job in result:
        try:
            salary.add(int(job["min_salary"]))
        except ValueError:
            pass

    min_salary = min(salary)
    return min_salary


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError()
    elif (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError()
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError()
    elif job["min_salary"] <= salary <= job["max_salary"]:
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

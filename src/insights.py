from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    types = []

    for t in jobs:
        if types.__contains__(t["job_type"]) is False:
            types.append(t["job_type"])
    return types


def filter_by_job_type(jobs, job_type):
    filtered_job_typy = [r for r in jobs if r["job_type"] == job_type]
    return filtered_job_typy


def get_unique_industries(path):
    file_content = read(path)
    inds = []

    for i in file_content:
        if inds.__contains__(i["industry"]) is False and i["industry"] != "":
            inds.append(i["industry"])

    return inds


def filter_by_industry(jobs, industry):
    filtered_by_industry = [r for r in jobs if r["industry"] == industry]
    return filtered_by_industry


def get_max_salary(path):
    salaries = read(path)
    max_salaries = set()

    for s in salaries:
        if s["max_salary"] != "invalid" and s["max_salary"] != "":
            max_salaries.add(int(s["max_salary"]))
    return max(max_salaries)
    pass


def get_min_salary(path):
    salaries = read(path)
    min_salaries = set()

    for s in salaries:
        if s["min_salary"] != "invalid" and s["min_salary"] != "":
            min_salaries.add(int(s["min_salary"]))
    return min(min_salaries)
    pass


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError("No row match found")
    elif (
        not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or not isinstance(salary, int)
    ):
        raise ValueError("Non-numeric values found")
    elif job["max_salary"] < job["min_salary"]:
        raise ValueError("Max salary must be bigger than Min salary")
    elif job["max_salary"] >= salary >= job["min_salary"]:
        return True
    else:
        return False
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

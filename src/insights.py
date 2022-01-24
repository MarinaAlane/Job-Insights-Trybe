from src.jobs import read


def get_unique_job_types(path):
    list_of_dicts_from_csv = read(path)

    job_types = set()
    for job in list_of_dicts_from_csv:
        job_types.add(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs_by_type = []

    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs_by_type.append(job)

    return filtered_jobs_by_type


def get_unique_industries(path):
    list_of_dicts_from_csv = read(path)

    industries = set()
    for job in list_of_dicts_from_csv:
        if job["industry"] != "":
            industries.add(job["industry"])

    return industries


def filter_by_industry(jobs, industry):
    filtered_jobs_by_industry = []

    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs_by_industry.append(job)

    return filtered_jobs_by_industry


def get_max_salary(path):
    list_of_dicts_from_csv = read(path)

    salaries = []
    for job in list_of_dicts_from_csv:
        if job["max_salary"].isdigit():
            salaries.append(int(job["max_salary"]))

    max_salary = max(salaries)

    return max_salary


def get_min_salary(path):
    list_of_dicts_from_csv = read(path)

    salaries = []
    for job in list_of_dicts_from_csv:
        if job["min_salary"].isdigit():
            salaries.append(int(job["min_salary"]))

    min_salary = min(salaries)

    return min_salary


def matches_salary_range(job, salary=int):
    min_salary = job["min_salary"]
    max_salary = job["max_salary"]

    if min_salary is None or max_salary is None:
        raise ValueError
    elif not type(min_salary) == int or (max_salary) == int:
        raise ValueError
    elif min_salary > max_salary:
        raise ValueError

    is_in_range = True
    print(f"min_salary: {min_salary}")
    print(f"salary: {salary}")
    print(f"max_salary: {max_salary}")
    if salary < min_salary or salary > max_salary:
        is_in_range = False

    return is_in_range


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

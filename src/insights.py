from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    jobs_unique_types = set()

    for job in jobs_list:
        jobs_unique_types.add(job["job_type"])

    return jobs_unique_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = [job for job in jobs if job["job_type"] == job_type]
    return filtered_jobs


def get_unique_industries(path):
    jobs_list = read(path)
    unique_industries = set()

    for job in jobs_list:
        if job["industry"]:
            unique_industries.add(job["industry"])

    return unique_industries


def filter_by_industry(jobs, industry):
    filtered_industries = [job for job in jobs if job["industry"] == industry]
    return filtered_industries


def get_max_salary(path):
    jobs_list = read(path)
    salaries = set()

    for job in jobs_list:
        if job["max_salary"].isnumeric():
            salaries.add(int(job["max_salary"]))

    return max(salaries)


def get_min_salary(path):
    jobs_list = read(path)
    salaries = set()

    for job in jobs_list:
        if job["min_salary"].isnumeric():
            salaries.add(int(job["min_salary"]))

    return min(salaries)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    elif (
        type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
        or type(salary) is not int
    ):
        raise ValueError
    elif job["min_salary"] > job["max_salary"]:
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
    jobs_on_salary_range = list()

    for job in jobs:
        try:
            is_valid_salary = matches_salary_range(job, salary)
            if is_valid_salary:
                jobs_on_salary_range.append(job)
        except ValueError:
            pass

    return jobs_on_salary_range

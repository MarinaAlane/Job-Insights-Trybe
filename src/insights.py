from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)

    job_types = set(job["job_type"] for job in jobs)

    return job_types


def filter_by_job_type(jobs, job_type):
    filter_job = list()

    for job in jobs:
        if job["job_type"] == job_type:
            filter_job.append(job)

    return filter_job


def get_unique_industries(path):
    jobs = read(path)

    industries = set()

    for industry in jobs:
        if industry["industry"] != "":
            industries.add(industry["industry"])

    return industries


def filter_by_industry(jobs, industry):
    filter_job = list()

    for job in jobs:
        if job["industry"] == industry:
            filter_job.append(job)

    return filter_job


def get_max_salary(path):
    jobs = read(path)

    salaries = list()
    # http://www.w3big.com/pt/python/att-string-isnumeric.html
    for salary in jobs:
        if salary["max_salary"].isnumeric():
            salaries.append(int(salary["max_salary"]))

    return max(salaries)


def get_min_salary(path):
    jobs = read(path)

    salaries = set()

    for salary in jobs:
        if salary["min_salary"].isnumeric():
            salaries.add(int(salary["min_salary"]))

    return min(salaries)


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError
    elif (
        type(salary) != int
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
    ):
        raise ValueError
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError
    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    job_list = list()

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                job_list.append(job)
        except ValueError:
            pass
    return job_list

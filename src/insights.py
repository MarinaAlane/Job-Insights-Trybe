from src import jobs


def get_unique_job_types(path):
    job_types = []
    for job in jobs.read(path):
        job_types.append(job["job_type"])
    return list(set(job_types))


def filter_by_job_type(jobs, job_type):
    """
    references:
    https://www.pythontutorial.net/python-basics/python-filter-list/"""
    job_by_type = list(filter(lambda job: job["job_type"] == job_type, jobs))
    return job_by_type


def get_unique_industries(path):
    industries = []
    for job in jobs.read(path):
        if job["industry"] == "" or job["industry"] in industries:
            pass
        else:
            industries.append(job["industry"])
    return list(set(industries))


def filter_by_industry(jobs, industry):
    ind_by_job = filter(lambda job: job["industry"] == industry, jobs)
    return list(ind_by_job)


def get_max_salary(path):
    biggest_salary = 0
    for job in jobs.read(path):
        if job["max_salary"] == "" or not job["max_salary"].isdigit():
            continue
        elif int(job["max_salary"]) > biggest_salary:
            biggest_salary = int(job["max_salary"])
    return biggest_salary


def get_min_salary(path):
    smallest_salary = get_max_salary(path)
    for job in jobs.read(path):
        if job["min_salary"] == "" or not job["min_salary"].isdigit():
            continue
        elif int(job["min_salary"]) < smallest_salary:
            smallest_salary = int(job["min_salary"])
    return smallest_salary


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Job doesn't have min_salary or max_salary")
    elif (
        not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or not isinstance(salary, int)
    ):
        raise ValueError("Job min_salary or max_salary is not an integer")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary is greater than max_salary")
    elif salary < job["min_salary"] or salary > job["max_salary"]:
        return False
    else:
        return True


def filter_by_salary_range(jobs, salary):
    filter_salary_range = list()

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_salary_range.append(job)
        except ValueError:
            pass
    return filter_salary_range

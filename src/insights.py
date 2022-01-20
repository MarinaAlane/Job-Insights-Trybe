from .jobs import read


def get_unique_job_types(path):
    data = read(path)
    job_types = set()
    for job in data:
        job_types.add(job["job_type"])

    return list(job_types)


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    data = read(path)
    industries = set()
    for job in data:
        if job["industry"] != "":
            industries.add(job["industry"])
    return list(industries)


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    data = read(path)
    max_salary = 0
    for job in data:
        if job["max_salary"].isnumeric():
            if int(job["max_salary"]) > max_salary:
                max_salary = int(job["max_salary"])

    return int(max_salary)


def get_min_salary(path):
    data = read(path)
    min_salary = get_max_salary(path)
    for job in data:
        if job["min_salary"].isnumeric():
            if int(job["min_salary"]) < min_salary:
                min_salary = int(job["min_salary"])

    return int(min_salary)


def matches_salary_range(job, salary):
    if not ("max_salary" in job and "min_salary" in job):
        raise ValueError("Salário mínimo e máximo são obrigatórios")
    if (type(job["max_salary"]) is not int or
            type(job["min_salary"]) is not int):
        raise ValueError("min and max salary must be int")
    if (job["max_salary"] < job["min_salary"]):
        raise ValueError
    if (type(salary) is not int):
        raise ValueError
    return job["max_salary"] >= salary >= job["min_salary"]


def filter_by_salary_range(jobs, salary):
    result = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                result.append(job)
        except ValueError:
            pass
    return result

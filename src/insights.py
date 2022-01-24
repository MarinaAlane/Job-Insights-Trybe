from .jobs import read


def get_unique_job_types(path):
    listJobs = read(path)
    setJobs = set()
    for job in listJobs:
        setJobs.add(job["job_type"])
    return setJobs


def filter_by_job_type(jobs, job_type):
    return [j for j in jobs if j["job_type"] == job_type]


def get_unique_industries(path):
    listJobs = read(path)
    setJobs = set()
    for job in listJobs:
        if "industry" in job:
            if job["industry"] != "":
                setJobs.add(job["industry"])
    return setJobs


def filter_by_industry(jobs, industry):
    return [j for j in jobs if j["industry"] == industry]


def get_max_salary(path):
    listJobs = read(path)
    value = 0
    for job in listJobs:
        if job["max_salary"] != "" and job["max_salary"].isnumeric():
            if int(job["max_salary"]) > value:
                value = int(job["max_salary"])
    return value


def get_min_salary(path):
    listJobs = read(path)
    value = get_max_salary(path)
    for job in listJobs:
        if job["min_salary"] != "" and job["min_salary"].isnumeric():
            if int(job["min_salary"]) < value:
                value = int(job["min_salary"])
    return value


def matches_salary_range(job, salary):
    if not isinstance(salary, int):
        raise ValueError
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    if (
        type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
    ):
        raise ValueError
    if int(job["min_salary"]) > int(job["max_salary"]):
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

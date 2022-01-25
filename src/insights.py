from src.jobs import read


def get_unique_job_types(path):
    job_types = set()
    jobs = read(path)
    for job in jobs:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    job_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_list.append(job)
    return job_list


def get_unique_industries(path):
    jobs = read(path)
    values_industry = set()
    for job in jobs:
        if job["industry"] != "":
            values_industry.add(job["industry"])

    return values_industry


def filter_by_industry(jobs, industry):
    list_industry = []

    for job in jobs:
        if job["industry"] == industry:
            list_industry.append(job)
    return list_industry


def get_max_salary(path):
    max_salary = 0
    jobs = read(path)
    for job in jobs:
        job_salary = job["max_salary"]
        if (
            job_salary != ""
            and job_salary != "invalid"
            and int(job["max_salary"]) > max_salary
        ):
            max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path):
    mim_salary = []
    jobs = read(path)
    for job in jobs:
        job_salary = job["min_salary"]
        if job_salary != "" and job_salary != "invalid":
            mim_salary.append(int(job["min_salary"]))
    mim_salary.sort()
    return mim_salary[0]


def matches_salary_range(job, salary):
    if "min_salary" not in job.keys() or "max_salary" not in job.keys():
        raise ValueError()
    if not isinstance(job["min_salary"], int) or not isinstance(
        job["max_salary"], int
    ):
        raise ValueError()
    if job["min_salary"] > job["max_salary"]:
        raise ValueError()
    if not isinstance(salary, int):
        raise ValueError()
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    list_jobs = []
    for job in jobs:
        if (
            isinstance(job["min_salary"], int)
            and isinstance(job["max_salary"], int)
            and job["min_salary"] < job["max_salary"]
            and (isinstance(salary, int))
            and matches_salary_range(job, salary)
        ):
            list_jobs.append(job)
    return list_jobs


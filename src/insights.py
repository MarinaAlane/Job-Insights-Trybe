from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    jobs = set()
    for job in data:
        jobs.add(job["job_type"])
    return jobs


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    data = read(path)
    industries = set()
    for information in data:
        if (information["industry"] != ""):
            industries.add(information["industry"])
    return industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    data = read(path)
    salaries = []
    for information_salary in data:
        if (information_salary["max_salary"].isdigit()):
            salary = (information_salary["max_salary"])
            salaries.append(int(salary))
    return max(salaries)


def get_min_salary(path):
    data = read(path)
    salaries = []
    for information_salary in data:
        if (information_salary["min_salary"].isdigit()):
            salary = (information_salary["min_salary"])
            salaries.append(int(salary))
    return min(salaries)


def matches_salary_range(job, salary):
    if("max_salary" not in job or "min_salary" not in job):
        raise ValueError
    elif(
        not type(job["min_salary"]) is int or
        not type(job["max_salary"]) is int or
        not type(salary) is int
    ):
        raise ValueError
    elif(job["min_salary"] >= job["max_salary"]):
        raise ValueError
    return (job["min_salary"] <= salary <= job["max_salary"])


def filter_by_salary_range(jobs, salary):
    jobs_list = []
    for job in jobs:
        try:
            if (matches_salary_range(job, salary)):
                jobs_list.append(job)
        except ValueError:
            continue
    return jobs_list

from src.jobs import read
# from importlib.resources import path


def get_unique_job_types(path):
    jobs_list = read(path)
    jobs_types = set()
    for job in jobs_list:
        jobs_types.add(job["job_type"])
    return list(jobs_types)


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    industries_list = read(path)
    industries_types = set()
    for industry in industries_list:
        if not industry["industry"] == "":
            industries_types.add(industry["industry"])
    return list(industries_types)


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    salaries_list = read(path)
    max_salaries = []
    for salary in salaries_list:
        salaries = salary["max_salary"]
        if salaries.isdigit():
            max_salaries.append(int(salaries))
    return max(max_salaries)


def get_min_salary(path):
    salaries_list = read(path)
    min_salaries = set()
    for salary in salaries_list:
        salaries = salary["min_salary"]
        if salaries.isdigit():
            min_salaries.add(int(salaries))
    return min(min_salaries)


def matches_salary_range(job, salary):
    for value in job:
        if "min_salary" and "max_salary" not in job or type(job[value]) != int:
            raise ValueError()

    if job["min_salary"] > job["max_salary"] or not (isinstance(salary, int)):
        raise ValueError()

    return salary >= job["min_salary"] and salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    jobs_by_salary = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_by_salary.append(job)
        except ValueError:
            print(f"{job} invalid")

    return jobs_by_salary

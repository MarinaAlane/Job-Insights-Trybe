from src.jobs import read


def get_unique_job_types(path):
    content = read(path)
    jobs_type = []
    for row in content:
        if row["job_type"] not in jobs_type:
            jobs_type.append(row["job_type"])
    return jobs_type


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    content = read(path)
    industries = []
    for row in content:
        if row["industry"] not in industries and row["industry"] != "":
            industries.append(row["industry"])
    return industries


def filter_by_industry(jobs, industry):
    filtered_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs.append(job)
    return filtered_jobs


def get_max_salary(path):
    content = read(path)
    salaries = []
    for row in content:
        # https://www.w3schools.com/python/ref_string_isdigit.asp
        if row["max_salary"].isdigit():
            salaries.append(int(row["max_salary"]))
    return max(salaries)


def get_min_salary(path):
    content = read(path)
    salaries = []
    for row in content:
        if row["min_salary"].isdigit():
            salaries.append(int(row["min_salary"]))
    return min(salaries)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError()
    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError()
    elif type(salary) != int:
        raise ValueError()
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError()

    it_matches = job["min_salary"] <= salary <= job["max_salary"]
    return it_matches


def filter_by_salary_range(jobs, salary):
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass
    return filtered_jobs

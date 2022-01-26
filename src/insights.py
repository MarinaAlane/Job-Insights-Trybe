from src.jobs import read


def get_unique_job_types(path):
    file_content = read(path)
    unique_jobs_types = []

    for row in file_content:
        if row["job_type"] not in unique_jobs_types:
            unique_jobs_types.append(row["job_type"])

    return unique_jobs_types


def filter_by_job_type(jobs, job_type):
    jobs_filtered = []

    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filtered.append(job)

    return jobs_filtered


def get_unique_industries(path):
    file_content = read(path)
    unique_industries = []

    for row in file_content:
        if row["industry"] not in unique_industries and row["industry"] != "":
            unique_industries.append(row["industry"])

    return unique_industries


def filter_by_industry(jobs, industry):
    jobs_filtered = []

    for job in jobs:
        if job["industry"] == industry:
            jobs_filtered.append(job)

    return jobs_filtered


def get_max_salary(path):
    file_content = read(path)
    max_salaries = set()

    for row in file_content:
        if row["max_salary"].isnumeric():
            max_salaries.add(int(row["max_salary"]))

    return max(max_salaries)


def get_min_salary(path):
    file_content = read(path)
    min_salaries = set()

    for row in file_content:
        if row["min_salary"].isnumeric():
            min_salaries.add(int(row["min_salary"]))

    return min(min_salaries)


def matches_salary_range(job, salary):
    if not ("max_salary" in job and "min_salary" in job):
        raise ValueError("Job does not have a salary range")
    elif (
      type(job["max_salary"]) is not int or
      type(job["min_salary"]) is not int or
      type(salary) is not int
    ):
        raise ValueError("Salary must be an integer")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary is greater than max_salary")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    jobs_filtered = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_filtered.append(job)
        except ValueError:
            pass

    return jobs_filtered

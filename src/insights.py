from src.jobs import read


def get_unique_job_types(path):
    csv_file = read(path)

    list_jobs = []
    for row in csv_file:
        list_jobs.append(row["job_type"])

    return list(dict.fromkeys(list_jobs))


def filter_by_job_type(jobs, job_type):
    jobs_filtered = []

    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filtered.append(job)

    return jobs_filtered


def get_unique_industries(path):
    csv_file = read(path)

    list_industries = []
    for row in csv_file:
        if row["industry"] != '':
            list_industries.append(row["industry"])

    return list(dict.fromkeys(list_industries))


def filter_by_industry(jobs, industry):
    industry_filtered = []

    for business in jobs:
        if business["industry"] == industry:
            industry_filtered.append(business)

    return industry_filtered


def get_max_salary(path):
    csv_file = read(path)

    list_max_salary = []

    for row in csv_file:
        if row["max_salary"].isdigit():
            list_max_salary.append(int(row["max_salary"], base=10))

    return max(list_max_salary, key=int) 


def get_min_salary(path):
    csv_file = read(path)

    list_min_salary = []

    for row in csv_file:
        if row["min_salary"].isdigit():
            list_min_salary.append(int(row["min_salary"], base=10))

    return min(list_min_salary, key=int)


def matches_salary_range(job, salary):

    pass


def filter_by_salary_range(jobs, salary):

    return []

from src import jobs


def get_unique_job_types(path):
    file = jobs.read(path)
    job_types_list = set()
    for row in file:
        if row["date_posted"]:
            job_types_list.add(row["date_posted"])
    return job_types_list


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    file = jobs.read(path)
    industries_list = set()
    for row in file:
        if row["industry"]:
            industries_list.add(row["industry"])
    return industries_list


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    file = jobs.read(path)
    salary = 0
    for job in file:
        if job["max_salary"].isnumeric() and int(job["max_salary"]) > salary:
            salary = int(job["max_salary"])
    return salary


def get_min_salary(path):
    file = jobs.read(path)
    salary = get_max_salary("src/jobs.csv")
    for job in file:
        if job["min_salary"].isnumeric() and int(job["min_salary"]) < salary:
            salary = int(job["min_salary"])
    return salary


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError()
    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError()
    if job["min_salary"] > job["max_salary"]:
        raise ValueError()
    if type(salary) != int:
        raise ValueError()
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(jobs, salary):
    jobs_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list.append(job)
        except ValueError:
            pass
    return jobs_list

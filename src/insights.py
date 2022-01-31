from src import jobs


def get_unique_job_types(path):
    job_types = []
    for job in jobs.read(path):
        job_types.append(job["job_type"])
    return list(set(job_types))


def filter_by_job_type(jobs, job_type):
    filtered_by_job_type = [job for job in jobs if job["job_type"] == job_type]
    return filtered_by_job_type


def get_unique_industries(path):
    job_data = jobs.read(path)
    job_industries = []
    for job in job_data:
        if job["industry"] != "" and job["industry"] not in job_industries:
            job_industries.append(job["industry"])
    return list(set(job_industries))


def filter_by_industry(jobs, industry):
    filtered_by_industry = [job for job in jobs if job["industry"] == industry]
    return filtered_by_industry


def get_max_salary(path):
    job_list = jobs.read(path)
    max_salary = 0
    for job in job_list:
        if (
            job["max_salary"].isnumeric()
            and int(job["max_salary"]) > max_salary
        ):
            max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path):
    job_list = jobs.read(path)
    min_salary = get_max_salary(path)
    for job in job_list:
        if (
            job["min_salary"].isnumeric()
            and int(job["min_salary"]) < min_salary
        ):
            min_salary = int(job["min_salary"])
    return min_salary


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError("Job does not have a salary range")
    if (
        type(salary) != int
        or type(job["max_salary"]) != int
        or type(job["min_salary"]) != int
    ):
        raise ValueError("Salary, min or max is not an integer")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("Min salary is greater than max salary")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filtered_by_salary_range = [
        job for job in jobs if matches_salary_range(job, salary)
    ]
    return filtered_by_salary_range

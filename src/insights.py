from src.jobs import read


def get_unique_job_types(path):
    job_type = set()
    jobs_list = read(path)
    for job in jobs_list:
        job_type.add(job["job_type"])
    return job_type


def filter_by_job_type(jobs, job_type):
    jobs_by_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_by_type.append(job)
    return jobs_by_type


def get_unique_industries(path):
    type_industries = set()
    jobs_list = read(path)
    for job in jobs_list:
        if len(job["industry"]) > 0:
            type_industries.add(job["industry"])
    return type_industries


def filter_by_industry(jobs, industry):
    jobs_by_industry = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_by_industry.append(job)
    return jobs_by_industry


def get_max_salary(path):
    max_salary_found = 0
    jobs_list = read(path)
    for job in jobs_list:
        salary = job["max_salary"]
        if salary.isdigit():
            if int(salary) > max_salary_found:
                max_salary_found = int(salary)

    return max_salary_found


def get_min_salary(path):
    min_salary_found = 0
    jobs_list = read(path)
    for job in jobs_list:
        salary = job["min_salary"]
        if salary.isdigit():
            if int(salary) < min_salary_found or min_salary_found == 0:
                min_salary_found = int(salary)

    return min_salary_found


def matches_salary_range(job, salary):

    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError("Chave max_salary ou min_salary ausentes")

    if type(job["max_salary"]) != int or type(job["min_salary"]) != int:
        raise ValueError("Chave max_salary ou min_salary não é um inteiro")

    if type(salary) != int:
        raise ValueError("Salary não é um inteiro")

    if job["max_salary"] > job["min_salary"]:
        return job["max_salary"] >= salary >= job["min_salary"]
    else:
        raise ValueError("max_salary deve ser maior que min_salary")


def filter_by_salary_range(jobs, salary):
    jobs_filtered_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_filtered_list.append(job)
        except ValueError:
            pass
    return jobs_filtered_list

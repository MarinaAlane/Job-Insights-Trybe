from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    jobs_types = set()
    for job in jobs:
        jobs_types.add(job["job_type"])
    return jobs_types


def filter_by_job_type(jobs, job_type):
    job_type_list = []

    for job in jobs:
        if job["job_type"] == job_type:
            job_type_list.append(job)

    return job_type_list


def get_unique_industries(path):
    jobs = read(path)
    industry_types = set()
    for job in jobs:
        if job["industry"] != "":
            industry_types.add(job["industry"])

    return industry_types


def filter_by_industry(jobs, industry):
    industry_list = []

    for job in jobs:
        if job["industry"] == industry:
            industry_list.append(job)

    return industry_list


def get_max_salary(path):
    jobs = read(path)
    salaries = set()
    for job in jobs:
        if job["max_salary"].isnumeric():
            salaries.add(int(job["max_salary"]))

    return max(list(salaries))


def get_min_salary(path):
    jobs = read(path)
    salaries = set()
    for job in jobs:
        if job["min_salary"].isnumeric():
            salaries.add(int(job["min_salary"]))

    return min(list(salaries))


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Salários não existem")
    elif (
        not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or not isinstance(salary, int)
    ):
        raise ValueError("entradas são inválidas")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary não pode ser maior que max_salary")
    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    salaries = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salaries.append(job)
        except ValueError:
            pass
    return salaries

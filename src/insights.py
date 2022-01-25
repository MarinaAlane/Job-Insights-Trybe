from src.jobs import read


def get_unique_job_types(path):
    arr = read(path)
    unique_arr = set()
    for job in arr:
        unique_arr.add(job["job_type"])

    return unique_arr


def filter_by_job_type(jobs, job_type):
    arr = []
    for job in jobs:
        if job["job_type"] == job_type:
            arr.append(job)

    return arr


def get_unique_industries(path):
    arr = read(path)
    industries_arr = set()
    for job in arr:
        if job['industry'] != '':
            industries_arr.add(job["industry"])

    return industries_arr


def filter_by_industry(jobs, industry):
    arr = []
    for job in jobs:
        if job["industry"] == industry:
            arr.append(job)

    return arr


def get_max_salary(path):
    arr = read(path)
    industries_arr = []
    for job in arr:
        if job['max_salary'] != '' and job['max_salary'].isnumeric():
            industries_arr.append(int(job['max_salary']))

    industries_arr.sort(reverse=True)
    return int(industries_arr[0])


def get_min_salary(path):
    arr = read(path)
    industries_arr = []
    for job in arr:
        if job['min_salary'] != '' and job['min_salary'].isnumeric():
            industries_arr.append(int(job['min_salary']))

    industries_arr.sort()
    return int(industries_arr[0])


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError("As chaves não existem")
    elif (
        type(job["max_salary"]) != int
        or type(job["min_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError("As chaves não são numericos")
    elif job["max_salary"] < job["min_salary"]:
        raise ValueError("Salario invalido")
    else:
        pass

    return salary >= job["min_salary"] and salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    jobs_arr = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_arr.append(job)
        except ValueError:
            pass

    return jobs_arr

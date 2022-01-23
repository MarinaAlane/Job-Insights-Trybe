from src.jobs import read


def get_unique_job_types(path):
    list = read(path)
    response = []
    for item in list:
        job_type = item["job_type"]
        if job_type and job_type not in response:
            response.append(job_type)

    return response


def filter_by_job_type(jobs, job_type):
    filtered = [job for job in jobs if job["job_type"] == job_type]

    return filtered


def get_unique_industries(path):
    list = read(path)
    response = []
    for item in list:
        industry = item["industry"]
        if industry and industry not in response:
            response.append(industry)

    return response


def filter_by_industry(jobs, industry):
    filtered = [job for job in jobs if job["industry"] == industry]

    return filtered


def get_max_salary(path):
    list = read(path)
    salaries = []
    for item in list:
        current_salary = item["max_salary"]
        if current_salary.isdigit():
            salaries.append(int(current_salary))

    return max(salaries)


def get_min_salary(path):
    list = read(path)
    salaries = []
    for item in list:
        current_salary = item["min_salary"]
        if current_salary.isdigit():
            salaries.append(int(current_salary))

    return min(salaries)


def matches_salary_range(job, salary):
    min = "min_salary"
    max = "max_salary"
    if max not in job or min not in job:
        raise ValueError
    elif type(job[min]) is not int and type(job[max]) is not int:
        raise ValueError
    elif job[min] > job[max]:
        raise ValueError
    elif type(salary) is not int:
        raise ValueError
    else:
        return job[min] <= salary and salary <= job[max]


def filter_by_salary_range(jobs, salary):
    filtered = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered.append(job)
        except ValueError:
            continue

    return filtered

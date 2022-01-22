from src.jobs import read


def get_unique_job_types(path):
    informations = read(path)
    unique_jobs = set()

    for information in informations:
        unique_jobs.add(information["job_type"])

    return list(unique_jobs)


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    informations = read(path)
    unique_industries = set()

    for information in informations:
        industry = information["industry"]
        if industry:
            unique_industries.add(industry)

    return list(unique_industries)


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    informations = read(path)
    only_salaries = list()

    for information in informations:
        salary = information["max_salary"]
        if salary.isdigit():
            only_salaries.append(int(salary))

    return max(only_salaries)


def get_min_salary(path):
    informations = read(path)
    only_salaries = list()

    for information in informations:
        salary = information["min_salary"]
        if salary.isdigit():
            only_salaries.append(int(salary))

    return min(only_salaries)


def matches_salary_range(job, salary):
    print(job, salary)
    keys_dict = ["min_salary", "max_salary"]

    for key in keys_dict:
        if key not in job or type(job[key]) != int:
            raise ValueError()

    if job["min_salary"] > job["max_salary"]:
        raise ValueError()

    return salary >= job["min_salary"] and salary <= job["max_salary"]



def filter_by_salary_range(jobs, salary):
    pass
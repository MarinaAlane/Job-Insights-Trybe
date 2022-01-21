from src.jobs import read


def get_unique_job_types(path):
    jobs_csv = read(path)
    jobs_cvs_types = set()
    for value_csv in jobs_csv:
        for job_index in value_csv["job_type"].split(","):
            jobs_cvs_types.add(job_index)
    return jobs_cvs_types


def filter_by_job_type(jobs, job_type):
    jobs_Types = []
    for job in jobs:
        if job['job_type'] == job_type:
            jobs_Types.append(job)
    return jobs_Types


def get_unique_industries(path):
    jobs = read(path)
    industries = set()
    for i in jobs:
        industry = i["industry"]
        if (industry != ''):
            industries.add(industry)
    return industries


def filter_by_industry(jobs, industry):
    Industries = []
    for job in jobs:
        if job['industry'] == industry:
            Industries.append(job)
    return Industries


def get_max_salary(path):
    jobs = read(path)
    max_salaries = []
    for item in jobs:
        if (item['max_salary'] != '' and item['max_salary'] != 'invalid'):
            max_salaries.append(int(item['max_salary']))
    max_salaries.sort()
    return max_salaries[-1]
# Rodolfo Rezende me ajudou na resolução dessa função


def get_min_salary(path):
    jobs = read(path)
    salary = []
    for item in jobs:
        if (item['min_salary'] != '' and item['min_salary'] != 'invalid'):
            salary.append(int(item['min_salary']))
    salary.sort()
    return salary[0]


def matches_salary_range(job, salary):
    if not ("min_salary" in job and "max_salary" in job):
        raise ValueError("min_salary and max_salary must be provided")

    elif not (
        isinstance(job["min_salary"], int)
        and
        isinstance(job["max_salary"], int)
    ):
        raise ValueError("min_salary and max_salary must be integers")

    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary can't be greater than max_salary")

    elif not isinstance(salary, int):
        raise ValueError("salary must be an integer")

    else:
        return job["min_salary"] <= salary <= job["max_salary"]
# Tales Coelho me ajudou na logica dessa questão


def filter_by_salary_range(jobs, salary):
    filter_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_salary.append(job)
        except ValueError:
            pass
    return filter_salary

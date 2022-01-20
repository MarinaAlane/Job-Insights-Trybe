from src.jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)
    job_types = set()
    for item in all_jobs:
        for job in item['job_type'].split(','):
            job_types.add(job)
    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job['job_type'] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    all_jobs = read(path)
    industry = set()
    for item in all_jobs:
        job = item['industry']
        if job != '':
            industry.add(item['industry'])
    return industry


def filter_by_industry(jobs, industry):
    filtered_industry = []
    for job in jobs:
        if job['industry'] == industry:
            filtered_industry.append(job)
    return filtered_industry


def get_max_salary(path):
    all_jobs = read(path)
    max_salary = int(0)
    for salary in all_jobs:
        curr_salary = salary['max_salary']
        if curr_salary != '' and curr_salary != 'invalid':
            int_curr_salary = int(curr_salary)
            if (int_curr_salary > max_salary):
                max_salary = int_curr_salary
    return max_salary


def get_min_salary(path):
    all_jobs = read(path)
    min_salary = 0
    for salary in all_jobs:
        curr_salary = salary['min_salary']
        if curr_salary != '' and curr_salary != 'invalid':
            if min_salary == 0:
                min_salary = int(curr_salary)
            int_curr_salary = int(curr_salary)
            if (int_curr_salary < min_salary):
                min_salary = int_curr_salary
    return min_salary


def matches_salary_range(job, salary):
    if not ('min_salary' in job and 'max_salary' in job):
        raise ValueError('min_salary e max_salary tem que existir')
    elif not (
        # achei esse isinstance no w3Schools
        isinstance(job['min_salary'], int)
        and
        isinstance(job['max_salary'], int)
    ):
        raise ValueError('min_salary e max_salary tem que ser do tipo int')
    elif job['min_salary'] > job['max_salary']:
        raise ValueError('min_salary não pode ser maior que o max_salary')
    elif not isinstance(salary, int):
        raise ValueError('salary tem que ser do tipo int')
    else:
        return job['min_salary'] <= salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):
    filter_by_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_by_salary.append(job)
        except ValueError:
            pass
    return filter_by_salary

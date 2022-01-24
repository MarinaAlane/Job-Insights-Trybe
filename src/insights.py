from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    jobs_types = set()
    for job in jobs:
        jobs_types.add(job['job_type'])
    return jobs_types


def filter_by_job_type(jobs, job_type):
    result = []
    for job in jobs:
        if job['job_type'] == job_type:
            result.append(job)
    return result


def get_unique_industries(path):
    industries = read(path)
    industries_unique = set([])
    for industry in industries:
        if industry['industry'] not in '':
            industries_unique.add(industry['industry'])
    return industries_unique


def filter_by_industry(jobs, industry):
    result = []
    for job in jobs:
        if job['industry'] == industry:
            result.append(job)
    return result


def get_max_salary(path):
    jobs = read(path)
    salaries = []
    for salary in jobs:
        if salary['max_salary'] != '' and salary['max_salary'] != 'invalid':
            salary_int = int(salary['max_salary'])
            salaries.append(salary_int)
    return max(salaries)


def get_min_salary(path):
    jobs = read(path)
    salaries = []
    for salary in jobs:
        if salary['min_salary'] != '' and salary['min_salary'] != 'invalid':
            salary_int = int(salary['min_salary'])
            salaries.append(salary_int)
    return min(salaries)


def matches_salary_range(job, salary):
    if (
        'min_salary' not in job or
        'max_salary' not in job or
        type(job['min_salary']) != int or
        type(job['max_salary']) != int or
        job['min_salary'] > job['max_salary'] or
        type(salary) != int
       ):
        raise ValueError
    return job['min_salary'] <= salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):
    list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list.append(job)
        except ValueError:
            ValueError
    return list

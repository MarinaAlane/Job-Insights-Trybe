from src.jobs import read
from src.helper.get_unique_func import get_unique_list_from_column
from src.helper.filter_by_column import filter_by_column
# from tokenize import Number
# from jobs import read
# from helper.get_unique_func import get_unique_list_from_column


def get_unique_job_types(path):
    jobs_list = read(path)
    data = get_unique_list_from_column(jobs_list, 'job_type')
    return data


def filter_by_job_type(jobs, job_type):
    data = filter_by_column(jobs, job_type, 'job_type')
    return data


def get_unique_industries(path):
    jobs_list = read(path)
    data = get_unique_list_from_column(jobs_list, 'industry')
    return data


def filter_by_industry(jobs, industry):
    data = filter_by_column(jobs, industry, 'industry')
    return data


def get_max_salary(path):
    jobs_list = read(path)
    salary = set()
    for job in jobs_list:
        if job['max_salary'].isnumeric():
            salary.add((int(job['max_salary'])))
            max_salary = max(salary)
    return max_salary


def get_min_salary(path):
    jobs_list = read(path)
    salary = set()
    for job in jobs_list:
        if job['min_salary'].isnumeric():
            salary.add((int(job['min_salary'])))
            min_salary = min(salary)
    return min_salary


def matches_salary_range(job, salary):
    if  not "min_salary" in job or "max_salary" not in job:
        raise ValueError
    min_salary = job['min_salary']
    max_salary = job['max_salary']
    if type(min_salary) != int or type(salary) != int \
                or type(max_salary) != int:
            raise ValueError
    if job["min_salary"] > job["max_salary"]:
        raise ValueError()
    else:
        return  min_salary <= salary <= max_salary

def filter_by_salary_range(jobs, salary):
    filtered_jobs = []
    for job in jobs:
        min_salary = job['min_salary']
        max_salary = job['max_salary']
        if type(min_salary) != int or type(salary) != int \
                or type(max_salary) != int:
            pass
        elif min_salary <= salary <= max_salary:
            filtered_jobs.append(job)
    return filtered_jobs

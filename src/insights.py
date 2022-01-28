from src.jobs import read
from .Utils.help_matches_salary_range import all_validations


def get_unique_job_types(path):

    return set([item["job_type"] for item in read(path)])


def filter_by_job_type(jobs, job_type):

    return [job for job in jobs if job['job_type'] == job_type]


def get_unique_industries(path):
    # all_ind = read(path)

    # ind = set()
    # for item in all_ind:
    #     industry = item['industry']
    #     if industry != '':
    #         ind.add(item['industry'])
    # print(ind)
    # # return ind
    return {ind["industry"] for ind in read(path) if ind['industry'] != ''}


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    all_salary = read(path)

    max_salary = []
    for item in all_salary:
        if (item["max_salary"] != '' and item['max_salary'] != 'invalid'):
            max_salary.append(int(item['max_salary']))
            max_salary.sort()
    print(max_salary[-1])
    return max_salary[-1]


def get_min_salary(path):
    all_salary = read(path)

    min_salary = []
    for item in all_salary:
        if (item["min_salary"] != '' and item['min_salary'] != 'invalid'):
            min_salary.append(int(item['min_salary']))
            min_salary.sort()
    print(min_salary[0])
    return min_salary[0]


def matches_salary_range(job, salary):
    all_validations(job, salary)
    if (job["min_salary"] <= salary <= job["max_salary"]):
        return True
    else:
        return False
        # Vini Gouveia me ajudou nesse requisito


def filter_by_salary_range(jobs, salary):
    filter_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_salary.append(job)
        except ValueError:
            pass
    return filter_salary

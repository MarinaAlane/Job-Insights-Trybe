from datetime import date

jobs = [ 
    {"min_salary": 10, "max_salary": 1000, "date_posted": "2021-01-24"},
    {"min_salary": 1000, "max_salary": 10000, "date_posted": "2020-01-24"},
    {"min_salary": '', "max_salary": '', "date_posted": ''},
]

sort_date = [
    {"min_salary": 10, "max_salary": 1000, "date_posted": "2021-01-24"},
    {"min_salary": 1000, "max_salary": 10000, "date_posted": "2020-01-24"},
    {"min_salary": '', "max_salary": '', "date_posted": ''},
]

sort_max_salary = [
    {"min_salary": 1000, "max_salary": 10000, "date_posted": "2020-01-24"},
    {"min_salary": 10, "max_salary": 1000, "date_posted": "2021-01-24"},
    {"min_salary": '', "max_salary": '', "date_posted": ''},
]

sort_min_salary = [
    {"min_salary": 1000, "max_salary": 10000, "date_posted": "2020-01-24"},
    {"min_salary": 10, "max_salary": 1000, "date_posted": "2021-01-24"},
    {"min_salary": '', "max_salary": '', "date_posted": ''},
]

def sort_by_any_criteria(jobs, criteria):

    valid_jobs = []
    invalid_jobs = []

    for job in jobs:
        if job.get(criteria, None):
            valid_jobs.append(job)
        else:
            invalid_jobs.append(job)

    if criteria in ['max_salary', 'min_salary']:
        valid_jobs.sort(key=lambda job: int(job[criteria]))
    else:
        valid_jobs.sort(key=lambda job: job[criteria])

    if criteria != 'min_salary':
        valid_jobs = valid_jobs[::-1]

    return valid_jobs + invalid_jobs


def sort_by_strings(jobs, criteria):

    if criteria not in ['max_salary', 'min_salary', 'date_posted']:
        raise ValueError

    valid_jobs = []
    invalid_jobs = []

    for job in jobs:
        if job.get(criteria, None):
            valid_jobs.append(job)
        else:
            invalid_jobs.append(job)

    reverse = criteria != "min_salary"

    valid_jobs.sort(key=lambda job: job[criteria], reverse=reverse)

    return valid_jobs + invalid_jobs


def sort_by_descending(jobs, criteria):

    if criteria not in ['max_salary', 'min_salary', 'date_posted']:
        raise ValueError

    valid_jobs = []
    invalid_jobs = []

    for job in jobs:
        if job.get(criteria, None):
            valid_jobs.append(job)
        else:
            invalid_jobs.append(job)

    if criteria in ["max_salary", "min_salary"]:
        valid_jobs.sort(key=lambda job: int(job[criteria]), reverse=True)
    elif criteria == "date_posted":
        valid_jobs.sort(key=lambda job: date(job[criteria]), reverse=True)

    return valid_jobs + invalid_jobs

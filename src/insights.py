from src.jobs import read


def get_unique_job_types(path):
    csv_data = read(path)

    job_types = set()
    job_types_list = []

    for job in csv_data:
        job_types.add(job['job_type'])

    for job_type in job_types:
        job_types_list.append(job_type)

    return job_types_list


def filter_by_job_type(jobs, job_type):
    jobs_by_job_type = []

    for job in jobs:
        if job['job_type'] == job_type:
            jobs_by_job_type.append(job)

    return jobs_by_job_type


def get_unique_industries(path):
    csv_data = read(path)

    industries = set()
    industries_list = []

    for industry in csv_data:
        industries.add(industry['industry'])

    for industry in industries:
        industries_list.append(industry)

    return list(filter(None, industries_list))


def filter_by_industry(jobs, industry):
    industries = []

    for job in jobs:
        if job['industry'] == industry:
            industries.append(job)

    return industries


def get_max_salary(path):
    csv_data = read(path)

    salaries_not_formatted = []
    salary_numbered_list = []

    for salary in csv_data:
        salaries_not_formatted.append(salary['max_salary'])

    salary_formatted = list(filter(None, salaries_not_formatted))

    for salary in salary_formatted:
        if salary != 'invalid':
            salary_numbered_list.append(int(salary))

    return (max(salary_numbered_list))


def get_min_salary(path):
    csv_data = read(path)

    salaries_not_formatted = []
    salary_numbered_list = []

    for salary in csv_data:
        salaries_not_formatted.append(salary['min_salary'])

    salary_formatted = list(filter(None, salaries_not_formatted))

    for salary in salary_formatted:
        if salary != 'invalid':
            salary_numbered_list.append(int(salary))

    return (min(salary_numbered_list))


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job or "max_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    jobs_by_salary_range = []

    for job in jobs:
        if matches_salary_range(job, salary):
            jobs_by_salary_range.append(job)

    return jobs_by_salary_range

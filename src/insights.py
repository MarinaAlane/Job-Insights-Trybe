from src.jobs import read


def get_unique_job_types(path):
    csv_array = read(path)
    csv_types = set()
    for item in csv_array:
        for job in item["job_type"].split(","):
            csv_types.add(job)
    return csv_types


def filter_by_job_type(jobs, job_type):
    filtered_job = []
    for job in jobs:
        if job['job_type'] == job_type:
            filtered_job.append(job)
    return filtered_job


def get_unique_industries(path):
    csv_array = read(path)
    industrias = set()
    for item in csv_array:
        industria = item["industry"]
        if (industria != ''):
            industrias.add(industria)
    return industrias


def filter_by_industry(jobs, industry):
    filtered_industry = []
    for job in jobs:
        if job['industry'] == industry:
            filtered_industry.append(job)
    return filtered_industry


def get_max_salary(path):
    csv_array = read(path)
    maior_salarios = []
    for item in csv_array:
        if (item['max_salary'] != '' and item['max_salary'] != 'invalid'):
            maior_salarios.append(int(item['max_salary']))
    maior_salarios.sort()
    return maior_salarios[-1]


def get_min_salary(path):
    csv_array = read(path)
    menor_salarios = []
    for item in csv_array:
        if (item['min_salary'] != '' and item['min_salary'] != 'invalid'):
            menor_salarios.append(int(item['min_salary']))
    menor_salarios.sort()
    print(menor_salarios)
    return menor_salarios[0]


def matches_salary_range(job, salary):
    keys = ['max_salary', 'min_salary']
    for key in keys:
        if key not in job or type(job[key]) != int:
            raise ValueError('min_salary or max_salary is not valid')

    if job['min_salary'] > job['max_salary']:
        raise ValueError("min_salary can't be greater than max_salary")

    return salary >= job['min_salary'] and salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):
    filtered_bysalary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_bysalary.append(job)
        except ValueError:
            pass
    return filtered_bysalary

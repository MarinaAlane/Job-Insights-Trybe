from src.jobs import read


def get_unique_job_types(path):
    listaUnica = read(path)
    job_type = []

    for row in listaUnica:
        if job_type.__contains__(row['job_type']) is False:
            job_type.append(row['job_type'])
    return job_type


def filter_by_job_type(jobs, job_type):

    list_job = [row for row in jobs if row['job_type'] == job_type]
    return list_job


def get_unique_industries(path):
    valore_unicos = read(path)
    ind = []
    bo = False

    for row in valore_unicos:
        if ind.__contains__(row['industry']) == bo and row['industry'] != '':
            ind.append(row['industry'])
    return ind


get_unique_industries('src/jobs.csv')


def filter_by_industry(jobs, industry):
    list_job = [row for row in jobs if row['industry'] == industry]
    return list_job


def get_max_salary(path):
    valore_unicos = read(path)
    max_s = set()

    for row in valore_unicos:
        if row['max_salary'] != '' and row['max_salary'] != 'invalid':
            max_s.add(int(row['max_salary']))

    return max(max_s)
    pass


def get_min_salary(path):
    valore_unicos = read(path)
    max_s = set()

    for row in valore_unicos:
        if row['min_salary'] != '' and row['min_salary'] != 'invalid':
            max_s.add(int(row['min_salary']))

    return min(max_s)
    pass


def matches_salary_range(job, salary):
    if 'max_salary' not in job or 'min_salary' not in job:
        raise ValueError('Chaves não existem')
    elif (
        not isinstance(job['min_salary'], int)
        or not isinstance(job['max_salary'], int)
        or not isinstance(salary, int)
    ):
        raise ValueError('Sem valor válido')
    elif job['max_salary'] < job['min_salary']:
        raise ValueError('max_salary é menor que min_salary')
    elif job["max_salary"] >= salary >= job['min_salary']:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    filtrados = []
    for todos_empregos in jobs:
        try:
            if matches_salary_range(todos_empregos, salary):
                filtrados.append(todos_empregos)
        except ValueError:
            pass
    return filtrados

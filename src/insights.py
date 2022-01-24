from .jobs import read


def get_unique_job_types(path):
    data = read(path)
    jobs_types = set()
    for job_type in data:
        jobs_types.add(job_type['job_type'])
    return jobs_types


def filter_by_job_type(jobs, job_type):
    jobs_filter_list = []
    for job in jobs:
        if(job['job_type'] == job_type):
            jobs_filter_list.append(job)
    return jobs_filter_list


def get_unique_industries(path):
    data = read(path)
    industries_types = set()
    for industry_type in data:
        if(industry_type['industry'] != ""):
            industries_types.add((industry_type['industry']))
    return industries_types


def filter_by_industry(jobs, industry):
    industry_filter_list = []
    for job in jobs:
        if(job['industry'] == industry):
            industry_filter_list.append(job)
    return industry_filter_list


def get_max_salary(path):
    data = read(path)
    list_salary = []
    for salary in data:
        if(salary['max_salary'] != "" and salary['max_salary'] != 'invalid'):
            list_salary.append(int(salary['max_salary']))
    max_salary = max(list_salary)
    return max_salary


def get_min_salary(path):
    data = read(path)
    list_salary = []
    for salary in data:
        if(salary['min_salary'] != "" and salary['min_salary'] != 'invalid'):
            list_salary.append(int(salary['min_salary']))
    min_salary = min(list_salary)
    return min_salary


def check_salary(job, salary):
    max_salary = job.get('max_salary', None)
    min_salary = job.get('min_salary', None)
    if(min_salary == "" or max_salary == ""):
        raise ValueError("falta valor")
    if(type(max_salary) is not int or type(min_salary) is not int):
        raise ValueError("valor não numerico")
    if(min_salary > max_salary):
        raise ValueError("valores invalidos")
    if(type(salary) is not int):
        raise ValueError("valor não numerico Salary")
    return


def matches_salary_range(job, salary):
    check_salary(job, salary)
    max_salary = job['max_salary']
    min_salary = job['min_salary']
    if(max_salary >= salary >= min_salary):
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []

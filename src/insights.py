from src.jobs import read


def get_unique_job_types(path):
    csv = read(path)
    job_type = set()
    for row in csv:
        job_type.add(row["job_type"])
    return job_type


def filter_by_job_type(jobs, job_type):
    filter_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filter_jobs.append(job)
    return filter_jobs


def get_unique_industries(path):
    csv = read(path)
    list = set()
    for item in csv:
        industry = item["industry"]
        if industry != '':
            list.add(industry)
    return list


def filter_by_industry(jobs, industry):
    filter_industry = []
    for job in jobs:
        if job["industry"] == industry:
            filter_industry.append(job)
    return filter_industry


def get_max_salary(path):
    csv = read(path)
    higher_salary = 0
    for item in csv:
        max_salary = item["max_salary"]
        if max_salary != '' and max_salary != 'invalid':
            if int(max_salary) > int(higher_salary):
                higher_salary = max_salary
    return int(higher_salary)


def get_min_salary(path):
    csv = read(path)
    salaries = []
    for item in csv:
        min_salary = item["min_salary"]
        if min_salary != '' and min_salary != 'invalid':
            salaries.append(int(min_salary))
    salaries.sort()
    return salaries[0]


def matches_salary_range(job, salary):
    min_salary = job["min_salary"]
    max_salary = job["max_salary"]
    if not ("min_salary" in job and "max_salary" in job):
        raise ValueError()
    if (type(min_salary) != int or type(max_salary) != int):
        raise ValueError()
    if (min_salary > max_salary):
        raise ValueError()
    if (type(salary) != int):
        raise ValueError()
    return min_salary <= salary <= max_salary


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

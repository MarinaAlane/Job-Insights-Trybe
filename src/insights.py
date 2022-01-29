import src.jobs as jobs


def get_unique_job_types(path):
    file = jobs.read(path)

    jobs_type = []
    for row in file:
        if row["job_type"] not in jobs_type:
            jobs_type.append(row["job_type"])
    return jobs_type


def filter_by_job_type(jobs, job_type):
    filter_job = []

    for job in jobs:
        if job["job_type"] == job_type:
            filter_job.append(job)
    return filter_job


def get_unique_industries(path):
    list = jobs.read(path)

    industry_type = []
    for row in list:
        if row["industry"] not in industry_type and row["industry"]:
            industry_type.append(row["industry"])
    return industry_type


def filter_by_industry(jobs, industry):
    filter_industry = []

    for job in jobs:
        if job["industry"] == industry:
            filter_industry.append(job)
    return filter_industry


def get_max_salary(path):
    list = jobs.read(path)

    max_salary = []
    for row in list:
        if row["max_salary"].isnumeric():
            max_salary.append(int(row["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    list = jobs.read(path)

    min_salary = []
    for row in list:
        if row["min_salary"].isnumeric():
            min_salary.append(int(row["min_salary"]))
    return min(min_salary)


def matches_salary_range(job, salary):
    if not ("min_salary" in job and "max_salary" in job):
        raise ValueError("Ausentes no dicionário")
    elif not (
        isinstance(job["min_salary"], int)
        and isinstance(job["max_salary"], int)
        and isinstance(salary, int)
    ):
        raise ValueError("Chave não númerica")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("Salário mínimo maior que o máximo")
    elif salary in range(job["min_salary"], job["max_salary"]):
        return True
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

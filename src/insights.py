from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_types = set()
    for job in jobs:
        if job["job_type"] != "":
            job_types.add(job["job_type"])
    return list(job_types)


# Solução para filtrar encontrada em:
# https://stackoverflow.com/questions/32474022/filter-list-of-dictionaries
def filter_by_job_type(jobs, job_type):
    if job_type == "":
        return []
    filtered_job_type = [job for job in jobs if job["job_type"] == job_type]
    return filtered_job_type


# Solução if encontrada em:
# https://stackoverflow.com/questions/54866974/
# what-is-efficient-way-of-removing-empty-values-from-dict-inside-list/54867063
def get_unique_industries(path):
    jobs = read(path)
    industry_types = set()
    for job in jobs:
        if job["industry"] != "":
            industry_types.add(job["industry"])
    return list(industry_types)


def filter_by_industry(jobs, industry):
    if industry == "":
        return []
    filtered_industry = [job for job in jobs if job["industry"] == industry]
    return filtered_industry


def get_max_salary(path):
    jobs = read(path)
    higher_salary = set()
    for salary in jobs:
        if salary["max_salary"].isdigit():
            higher_salary.add(int((salary["max_salary"])))
    return max(list(higher_salary))


def get_min_salary(path):
    jobs = read(path)
    lower_salary = set()
    for salary in jobs:
        if salary["min_salary"].isdigit():
            lower_salary.add(int((salary["min_salary"])))
    return min(list(lower_salary))


# Solução construída com a ajuda do instrutor Rhael Martim
def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("doesn't exists")
    elif (
        job["min_salary"] is None
        or job["max_salary"] is None
        or salary is None
    ):
        raise ValueError("aren't valid integers")
    elif (
        type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
        or type(salary) is not int
    ):
        raise ValueError("aren't valid integers")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("isn't a valid integer")
    else:
        return job["min_salary"] <= salary <= job["max_salary"]


# Solução construída com a ajuda do instrutor Rhael Martim
def filter_by_salary_range(jobs, salary):
    filtered_job_salary = []
    for job in jobs:
        try:
            filter_jobs = matches_salary_range(job, salary)
            if filter_jobs:
                filtered_job_salary.append(job)
        except ValueError as error:
            print(error)
    return filtered_job_salary

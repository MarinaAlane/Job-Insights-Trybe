from src import jobs


def get_unique_job_types(path):
    # utiliza a função feita no requisito 1
    data = jobs.read(path)

    # cria um set, pois se trata de um conjunto de elementos unicos
    types_of_jobs = set()
    for job in data:
        types_of_jobs.add(job["job_type"])
    return types_of_jobs


def filter_by_job_type(jobs, job_type):
    selected_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            selected_jobs.append(job)

    return selected_jobs


def get_unique_industries(path):
    data = jobs.read(path)
    industries = set()

    for job in data:
        if job["industry"]:
            industries.add(job["industry"])

    return industries


def filter_by_industry(jobs, industry):
    selected_industries = []
    for job in jobs:
        if job["industry"] == industry:
            selected_industries.append(job)

    return selected_industries


def get_max_salary(path):
    data = jobs.read(path)
    salaries = []

    for job in data:
        salary = job["max_salary"]
        if salary.isdigit():
            salaries.append(int(salary))

    return max(salaries)


def get_min_salary(path):
    data = jobs.read(path)
    salaries = []

    for job in data:
        salary = job["min_salary"]
        if salary.isdigit():
            salaries.append(int(salary))

    return min(salaries)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["max_salary"]) != int
        or type(job["min_salary"]) != int
        or job["max_salary"] < job["min_salary"]
        or type(salary) != int
    ):
        raise ValueError("invalid inputs")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    matched_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                matched_jobs.append(job)
        except ValueError:
            print("Error")

    return matched_jobs

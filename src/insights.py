from src.jobs import read


def get_unique_job_types(path):
    data = read(path)

    job_types = set()
    for row in data:
        job_types.add(row["job_type"])

    return list(job_types)


def filter_by_job_type(jobs, job_type):
    filtered = []
    for job in jobs:
        if job['job_type'] == job_type:
            filtered.append(job)

    return filtered


def get_unique_industries(path):
    data = read(path)

    industries = set()
    for row in data:
        industry = row["industry"]
        if industry:
            industries.add(industry)

    return list(industries)


def filter_by_industry(jobs, industry):
    filtered = []
    for job in jobs:
        if job['industry'] == industry:
            filtered.append(job)

    return filtered


def get_max_salary(path):
    datas = read(path)

    max_salaries = list()
    for data in datas:
        salary = data["max_salary"]
        if salary.isdigit():
            max_salaries.append(int(salary))

    return max(max_salaries)


def get_min_salary(path):
    datas = read(path)

    min_salaries = list()
    for data in datas:
        salary = data["min_salary"]
        if salary.isdigit():
            min_salaries.append(int(salary))

    return min(min_salaries)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or not job["min_salary"] < job["max_salary"]
        or not isinstance(salary, int)
    ):
        raise ValueError("error")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filtered = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered.append(job)
        except ValueError:
            print("Erro: Deu muito ruim!")

    return filtered

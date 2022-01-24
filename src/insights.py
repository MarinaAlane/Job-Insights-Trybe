from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    unique = {}
    for index in data:
        if not index["job_type"] in unique:
            unique[index["job_type"]] = 1
        else:
            unique[index["job_type"]] += 1
    return list(unique)


def filter_by_job_type(jobs, job_type):
    filtered = []
    for index in jobs:
        if index["job_type"] == job_type:
            filtered.append(index)
    return filtered


def get_unique_industries(path):
    data = read(path)
    industries = []
    for index in data:
        if index["industry"] != "":
            industries.append(index["industry"])
    return set(industries)


def filter_by_industry(jobs, industry):
    filtered = []
    for index in jobs:
        if index["industry"] == industry:
            filtered.append(index)
    return filtered


def get_max_salary(path):
    data = read(path)
    salaries = []
    for index in data:
        if index["max_salary"] != "" and index["max_salary"] != "invalid":
            salaries.append(float(int(index["max_salary"])))
    salaries.sort()
    return salaries[-1]


def get_min_salary(path):
    data = read(path)
    salaries = []
    for index in data:
        if index["min_salary"] != "" and index["min_salary"] != "invalid":
            salaries.append(float(int(index["min_salary"])))
    salaries.sort()
    return salaries[0]


def matches_salary_range(job, salary):
    if not ("max_salary" in job and "min_salary" in job):
        raise ValueError("As chaves não estão no dict")
    elif (
        type(job["max_salary"]) != int
        or type(job["min_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError("Os valores não são inteiros")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError(
            "O valor de min_salary não pode ser maior que max_salary"
        )
    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    new_jobs = []
    for index in jobs:
        try:
            save = matches_salary_range(index, salary)
            if save:
                new_jobs.append(index)
        except ValueError:
            pass
    return new_jobs

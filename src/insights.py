from src.jobs import read


def get_unique_job_types(path):

    files = read(path)
    types = set()
    for row in files:
        types.add(row["job_type"])
    return types


def filter_by_job_type(jobs, job_type):

    filter_jobs = []
    for row in jobs:
        if (row["job_type"] == job_type):
            filter_jobs.append(row)

    return filter_jobs


def get_unique_industries(path):

    files = read(path)
    factories = set()
    for row in files:
        if (row["industry"]):
            factories.add(row["industry"])
    return factories


def filter_by_industry(jobs, industry):

    filtered = []
    for row in jobs:
        if (row["industry"] == industry):
            filtered.append(row)
    return filtered


def get_max_salary(path):

    files = read(path)
    salary = []
    for row in files:
        if (row["max_salary"] != "") and row["max_salary"] != "invalid":
            salary.append(int(float(row["max_salary"])))

    return max(salary)


def get_min_salary(path):

    files = read(path)
    salary = []
    for row in files:
        if (row["min_salary"] != "") and row["max_salary"] != "invalid":
            salary.append(int(float(row["min_salary"])))

    return min(salary)


def matches_salary_range(job, salary):

    if ("min_salary" not in job or "max_salary" not in job):
        raise ValueError
    elif (
        type(job["min_salary"]) != int or
        type(job["max_salary"]) != int or
        type(salary) != int
    ):
        raise ValueError
    elif (job["min_salary"] > job["max_salary"]):
        raise ValueError
    elif (job["min_salary"] <= salary <= job["max_salary"]):
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):

    filter_salaries = []
    for row in jobs:
        try:

            if matches_salary_range(row, salary):
                filter_salaries.append(row)
        except ValueError:
            pass

    return filter_salaries

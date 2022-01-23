from src.jobs import read


def get_unique_job_types(path):
    try:
        jobs = read(path)
        types = set()
        for job in jobs:
            if (job["job_type"] != ""):
                types.add(job["job_type"])
        return types
    except FileNotFoundError:
        print("File not fount!!!")


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    try:
        for job in jobs:
            if (job["job_type"] == job_type):
                filtered_jobs.append(job)
    except ValueError:
        print("The value of argument is invalid!!!")
    return filtered_jobs


def get_unique_industries(path):
    try:
        jobs = read(path)
        factories = set()
        for factory in jobs:
            if (factory["industry"] != ""):
                factories.add(factory["industry"])
        return factories
    except FileNotFoundError:
        print("File not fount!!!")


def filter_by_industry(jobs, industry):
    filtered_industries = []
    try:
        for industry in jobs:
            if (industry["industry"] == industry):
                filtered_industries.append(industry)
    except ValueError:
        print("The value of argument is invalid!!!")
    return filtered_industries


def get_max_salary(path):
    jobs = read(path)
    salaries = []
    for salary in jobs:
        try:
            if (salary["max_salary"] != ""):
                salaries.append(int(float(salary["max_salary"])))
        # https://docs.python.org/pt-br/3/library/exceptions.html#ValueError
        except ValueError:
            print("The value of argument is invalid!!!")
    return max(salaries)


def get_min_salary(path):
    jobs = read(path)
    salaries = []
    for salary in jobs:
        try:
            if (salary["min_salary"] != ""):
                salaries.append(int(float(salary["min_salary"])))
        except ValueError:
            print("The value of argument is invalid!!!")
    return min(salaries)


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
    filtered_salaries = []
    for salaries in jobs:
        try:
            if (matches_salary_range(salaries, salary)):
                filtered_salaries.append(salaries)
        except ValueError:
            print("The value of argument is invalid!!!")
    return filtered_salaries

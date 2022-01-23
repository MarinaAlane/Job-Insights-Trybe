from src.jobs import read
# from jobs import read


def get_unique_job_types(path):
    get_read = read(path)
    job_types = []

    for res in get_read:
        if res["job_type"] not in job_types:
            job_types.append(res["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []

    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs


def get_unique_industries(path):
    get_read = read(path)
    unique_industries = []

    for res in get_read:
        if res["industry"] \
          not in unique_industries \
          and len(res["industry"]) != 0:
            unique_industries.append(res["industry"])

    return unique_industries


def filter_by_industry(jobs, industry):
    filtered_industry = []

    for job in jobs:
        if job["industry"] == industry:
            filtered_industry.append(job)

    return filtered_industry


def get_max_salary(path):
    get_read = read(path)
    max_salary = 0

    for res in get_read:
        if len(res["max_salary"]) \
          and res["max_salary"].isnumeric():
            salary = int(res["max_salary"])
            if salary > max_salary:
                max_salary = salary

    return max_salary


def get_min_salary(path):
    get_read = read(path)
    min_salary = 9999999

    for res in get_read:
        if len(res["min_salary"]) \
          and res["min_salary"].isnumeric():
            salary = int(res["min_salary"])
            if salary < min_salary:
                min_salary = salary

    return min_salary


def matches_salary_range(job, salary):
    if "min_salary" not in job \
      or "max_salary" not in job:
        raise ValueError("invalid params")

    min_salary = job["min_salary"]
    max_salary = job["max_salary"]

    if type(min_salary) != int \
       or type(max_salary) != int:
        raise ValueError("invalid type jobs")

    if min_salary > max_salary:
        raise ValueError("invalid salary range")

    if type(salary) != int:
        raise ValueError("invalid type salary")

    return min_salary <= salary <= max_salary


jobs = [
    {"max_salary": 0, "min_salary": 10},
    {"max_salary": 10, "min_salary": 100},
    {"max_salary": 10000, "min_salary": 200},
    {"max_salary": 15000, "min_salary": 0},
    {"max_salary": 1500, "min_salary": 0},
    {"max_salary": -1, "min_salary": 10},
]


def filter_by_salary_range(jobs, salary):
    passedJobs = []

    for job in jobs:
        if type(salary) == int and salary is not None:
            if type(job["min_salary"]) or type(job["max_salary"]) == int:
                if type(job["min_salary"]) \
                  or type(job["max_salary"]) is not None:
                    if job["min_salary"] <= salary <= job["max_salary"]:
                        passedJobs.append(job)

    return passedJobs


# result = filter_by_salary_range(jobs, 1000)

# print(result)

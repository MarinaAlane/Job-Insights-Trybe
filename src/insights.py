from src.jobs import read


def get_unique_job_types(path):
    csv_list = read(path)
    job_types = set()
    for item in csv_list:
        for job in item["job_type"].split(","):
            job_types.add(job)
    return job_types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    csv_list = read(path)
    industries = set()
    for item in csv_list:
        industry = item["industry"]
        if industry != "":
            industries.add(industry)
    return industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    csv_list = read(path)
    max_salary = 0
    for item in csv_list:
        if (
            item["max_salary"] != ""
            and item["max_salary"] != "invalid"
            and int(item["max_salary"]) > max_salary
        ):
            max_salary = int(item["max_salary"])
    return max_salary


def get_min_salary(path):
    csv_list = read(path)
    min_salary = 100000000
    for item in csv_list:
        if (
            item["min_salary"] != ""
            and item["min_salary"] != "invalid"
            and int(item["min_salary"]) < min_salary
        ):
            min_salary = int(item["min_salary"])
    return min_salary


def matches_salary_range(job, salary):
    if type(salary) != int:
        raise ValueError
    keys_of_job = ["min_salary", "max_salary"]
    for key in keys_of_job:
        if key not in job or type(job[key]) != int:
            raise ValueError
    if job["min_salary"] > job["max_salary"]:
        raise ValueError
    return salary >= job["min_salary"] and salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    valid_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                valid_jobs.append(job)
        except ValueError:
            print("job invalido my friend")
    return valid_jobs

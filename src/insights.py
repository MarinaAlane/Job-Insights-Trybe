from .jobs import read


def get_unique_job_types(path):
    jobs_csv = read(path)
    job_types_from_csv = set()

    for job in jobs_csv:
        job_types_from_csv.add(job["job_type"])          
    return job_types_from_csv


def filter_by_job_type(jobs, job_type):
    filter_result = [job for job in jobs if job["job_type"] == job_type]

    return filter_result


def get_unique_industries(path):
    jobs_industries_csv = read(path)
    job_industry = set()

    for job in jobs_industries_csv:
        if job["insdustry"]:
            job_industry.add(job["industry"])

    return job_industry


def filter_by_industry(jobs, industry):
    filter_result = [job for job in jobs if job["industry"] == industry]

    return filter_result


def get_max_salary(path):
    jobs_salaries_csv = read(path)
    job_salary_from_csv = set()

    for job in jobs_salaries_csv:
        if job["max_salary"].isnumeric():
            job_salary_from_csv.add(int(job["max_salary"]))

    return max(job_salary_from_csv)


def get_min_salary(path):
    jobs_salaries_csv = read(path)
    job_salary_from_csv = set()

    for job in jobs_salaries_csv:
        if job["min_salary"].isnumeric():
            job_salary_from_csv.add(int(job["min_salary"]))

    return min(job_salary_from_csv)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError()
    if (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError()

    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError

    return int(job["min_salary"]) <= salary <= int(job["max_salary"])


def filter_by_salary_range(jobs, salary):
    data_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                data_salary.append(job)
        except ValueError:
            pass
    return data_salary

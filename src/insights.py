from src import jobs


def get_unique_job_types(path):
    jobs_dict = jobs.read(path)
    unique = list(set([job["job_type"] for job in jobs_dict]))

    return unique


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    jobs_dict = jobs.read(path)
    unique = list(
        set([job["industry"] for job in jobs_dict if job["industry"] != ""])
    )

    return unique


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    jobs_dict = jobs.read(path)
    salaries = list()
    for job in jobs_dict:
        try:
            salary = job["max_salary"]
            if salary != "":
                salaries.append(int(salary))
        except ValueError:
            pass

    salaries.sort(reverse=True)

    return salaries[0]


def get_min_salary(path):
    jobs_dict = jobs.read(path)
    salaries = list()
    for job in jobs_dict:
        try:
            salary = job["min_salary"]
            if salary != "":
                salaries.append(int(salary))
        except ValueError:
            pass

    salaries.sort()

    return salaries[0]


def matches_salary_range_error_handle(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError("max_salary and min_salary is required")

    elif (
        type(salary) != int
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
    ):
        raise ValueError("Only numbers are alowwed")

    elif job["max_salary"] < job["min_salary"]:
        raise ValueError("Invalid salary range")
    else:
        pass


def matches_salary_range(job, salary):
    matches_salary_range_error_handle(job, salary)
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filtered_jobs = list()

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass

    return filtered_jobs

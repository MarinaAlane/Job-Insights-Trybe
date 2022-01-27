from .jobs import read


def get_unique_job_types(path):
    data = read(path)
    unique_job_types = set()
    for job in data:
        unique_job_types.add(job["job_type"])
    print("Unique Job Types : ", unique_job_types)
    return unique_job_types


def filter_by_job_type(jobs, job_type):
    filtered_by_job_types = [
        job for job in jobs if job["job_type"] == job_type
    ]
    print("Filtered Job Types : ", filtered_by_job_types)
    return filtered_by_job_types


def get_unique_industries(path):
    data = read(path)
    unique_industries = set()
    for industries in data:
        if industries["industry"]:
            unique_industries.add(industries["industry"])
    print("Unique Industries : ", unique_industries)
    return unique_industries


def filter_by_industry(jobs, industry):
    filtered_by_industry = [job for job in jobs if job["industry"] == industry]
    print("Filtered Industries : ", filtered_by_industry)
    return filtered_by_industry


def get_max_salary(path):
    data = read(path)
    max_salary = set()
    for salaries in data:
        try:
            max_salary.add(int(salaries["max_salary"]))
        except ValueError:
            pass
    print("Max Salary : ", max(max_salary))
    return max(max_salary)


def get_min_salary(path):
    data = read(path)
    min_salary = set()
    for salaries in data:
        try:
            min_salary.add(int(salaries["min_salary"]))
        except ValueError:
            pass
    print("Min Salary : ", min(min_salary))
    return min(min_salary)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise (ValueError("doesn't exists"))
    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise (ValueError("aren't valid integers"))
    elif job["min_salary"] > job["max_salary"]:
        raise (ValueError("is greather than"))
    elif type(salary) != int:
        raise (ValueError("isn't a valid integer"))
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filtered_by_salary_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_by_salary_range.append(job)
        except ValueError:
            pass
    print("Filter By Salary Range : ", filtered_by_salary_range)
    return filtered_by_salary_range

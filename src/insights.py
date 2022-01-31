from cgitb import reset
import csv
from src.jobs import read


def get_unique_job_types(path):
    jobs_types = []
    jobs = read(path)
    for item in jobs:
        if not item["job_type"] in jobs_types:
            jobs_types.append(item["job_type"])
    return jobs_types


def filter_by_job_type(jobs, job_type):
    all_jobs_list = [job for job in jobs if job["job_type"] == job_type]
    return all_jobs_list


def get_unique_industries(path):
    all_jobs = read(path)
    industry_values = set()

    for item in all_jobs:
        if item["industry"] != "":
            industry_values.add(item["industry"])

    return industry_values


def filter_by_industry(jobs, industry):
    result = [job for job in jobs if job["industry"] == industry]
    return result


def get_max_salary(path):
    with open(path) as jobs:
        max_salary = 0
        all_jobs_list = csv.DictReader(jobs)
        for item in all_jobs_list:
            if item["max_salary"].isdigit():
                if int(item["max_salary"]) > max_salary:
                    max_salary = int(item["max_salary"])
    return max_salary


def get_min_salary(path):
    with open(path) as jobs:
        min_salary = get_max_salary(path)
        all_jobs_list = csv.DictReader(jobs)
        for item in all_jobs_list:
            if item["min_salary"].isdigit():
                if int(item["min_salary"]) < min_salary:
                    min_salary = int(item["min_salary"])
    return min_salary


def matches_salary_range(job, salary):
    if (
        "max_salary" not in job or
        "min_salary" not in job or
        job["min_salary"] > job["max_salary"]
    ):
        raise ValueError

    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []

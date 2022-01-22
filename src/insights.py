from src import jobs
import math


def get_unique_job_types(path):
    jobs_list = jobs.read(path)
    unique_jobs = []
    for job in jobs_list:
        if job["job_type"] not in unique_jobs:
            unique_jobs.append(job["job_type"])

    return unique_jobs


def filter_by_job_type(jobs, job_type):

    return [job for job in jobs if job["job_type"] is job_type]


def get_unique_industries(path):
    jobs_list = jobs.read(path)
    unique_industries = set()
    for job in jobs_list:
        if job["industry"]:
            unique_industries.add(job["industry"])

    return unique_industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] is industry]


def get_max_salary(path):
    jobs_list = jobs.read(path)

    max_salary = 0
    for job in jobs_list:
        try:
            salary = int(job["max_salary"])
            if salary > max_salary:
                max_salary = salary
        except ValueError:
            pass
    return max_salary


def get_min_salary(path):
    jobs_list = jobs.read(path)

    # https://stackoverflow.com/questions/7781260/how-can-i-represent-an-infinite-number-in-python
    # Setar o valor de uma variável como infinito
    min_salary = math.inf
    for job in jobs_list:
        try:
            salary = int(job["min_salary"])
            if salary < min_salary:
                min_salary = salary
        except ValueError:
            pass
    return min_salary


def is_value_not_numeric(value):
    return type(value) is not int


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or is_value_not_numeric(job["min_salary"])
        or is_value_not_numeric(job["max_salary"])
        or is_value_not_numeric(salary)
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError

    return job["min_salary"] <= salary <= job["max_salary"]


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


if __name__ == "__main__":
    print(get_max_salary("jobs.csv"))

from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    jobs_filtered = set()

    [
        jobs_filtered.add(job['job_type'])
        for job in jobs
        if job['job_type'] != ""
    ]

    return jobs_filtered


def filter_by_job_type(jobs, job_type):
    filtered_job = [

        el for el in jobs if el['job_type'] == job_type
    ]

    return filtered_job


def get_unique_industries(path):
    jobs = read(path)
    industries = set()

    [
        industries.add(job['industry'])
        for job in jobs
        if job['industry'] != ""
    ]

    return industries


def filter_by_industry(jobs, industry):
    all_industries = list()

    [

        all_industries.append(el)

        for el in jobs

        if el['industry'] == industry

    ]

    return all_industries


def get_max_salary(path):
    jobs = read(path)

    job_salaries = set()

    [
        job_salaries.add(int(job['max_salary']))

        for job in jobs if job['max_salary']

        .isdigit()
    ]

    return max(job_salaries)


def get_min_salary(path):
    jobs = read(path)

    job_salaries = set()

    [
        job_salaries.add(int(job['min_salary']))

        for job in jobs

        if job['min_salary'].isdigit()

    ]

    return min(job_salaries)


def matches_salary_range(job, salary):
    if (

        type(salary) != int

            or "min_salary" not in job
            or "max_salary" not in job

            or type(job["min_salary"]) != int
            or type(job["max_salary"]) != int
            or job["min_salary"] > job["max_salary"]):

        raise ValueError("Value Error")

    salary = (job["max_salary"] >= salary >= job["min_salary"])

    return salary


def filter_by_salary_range(jobs, salary):

    filtered_salary = []

    for job in jobs:

        try:

            if matches_salary_range(job, salary):

                filtered_salary.append(job)

        except ValueError:

            pass

    return filtered_salary

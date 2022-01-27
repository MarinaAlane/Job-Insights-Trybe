from src.jobs import read


def get_unique_job_types(path):
    csv_file = read(path)

    list_jobs = []
    for row in csv_file:
        list_jobs.append(row["job_type"])

    return list(dict.fromkeys(list_jobs))


def filter_by_job_type(jobs, job_type):

    return []


def get_unique_industries(path):

    return []


def filter_by_industry(jobs, industry):

    return []


def get_max_salary(path):

    pass


def get_min_salary(path):

    pass


def matches_salary_range(job, salary):

    pass


def filter_by_salary_range(jobs, salary):

    return []

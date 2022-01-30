from src.jobs import read

# from jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    list_job_type = list()

    for job in jobs:
        if not job["job_type"] in list_job_type:
            list_job_type.append(job["job_type"])

    return list_job_type


def filter_by_job_type(jobs, job_type):
    list_jobs = list()

    for job in jobs:
        if job["job_type"] == job_type:
            list_jobs.append(job)

    return list_jobs


def get_unique_industries(path):
    industries = read(path)
    list_industries = list()

    for industry in industries:
        if (
            not industry["industry"] in list_industries
            and industry["industry"] != ""
        ):
            list_industries.append(industry["industry"])

    return list_industries


def filter_by_industry(jobs, industry):
    list_jobs_industries = list()

    for job in jobs:
        if job["industry"] == industry:
            list_jobs_industries.append(job)

    return list_jobs_industries


def get_max_salary(path):
    list_dict = read(path)
    salary_list = []
    for salary in list_dict:
        if salary["max_salary"].isdigit():
            salary_list.append(int(salary["max_salary"]))

    return max(salary_list)


def get_min_salary(path):

    list_dict = read(path)
    salary_list = []
    for salary in list_dict:
        if salary["min_salary"].isdigit():
            salary_list.append(int(salary["min_salary"]))

    return min(salary_list)


def matches_salary_range(job, salary):

    for value in job:
        if "min_salary" and "max_salary" not in job or type(job[value]) != int:
            raise ValueError()
    if job["min_salary"] > job["max_salary"] or type(salary) != int:
        raise ValueError()
    return salary >= job["min_salary"] and salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):

    salaries = list()

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salaries.append(job)
        except ValueError:
            print("Emprego inválido")

    return salaries

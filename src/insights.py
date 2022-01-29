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
    csv_file = read(path)

    list_industries = []
    for row in csv_file:
        if row["industry"] != '':
            list_industries.append(row["industry"])

    print(list(dict.fromkeys(list_industries)))
    
    return list(dict.fromkeys(list_industries))


def filter_by_industry(jobs, industry):

    return []


def get_max_salary(path):
    csv_file = read(path)

    list_max_salary = []

    for row in csv_file:
        if row["max_salary"].isdigit():
            list_max_salary.append(int(row["max_salary"], base=10))

    return max(list_max_salary, key=int) 


def get_min_salary(path):

    pass


def matches_salary_range(job, salary):

    pass


def filter_by_salary_range(jobs, salary):

    return []

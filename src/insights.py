from src import jobs


def get_unique_job_types(path):
    jobs_list = jobs.read(path)
    return list(set([job['job_type'] for job in jobs_list]))


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job['job_type'] == job_type]


def get_unique_industries(path):
    jobs_list = jobs.read(path)
    industries = set([
        job['industry'] for job in jobs_list if job['industry'] != ''])
    return list(industries)


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job['industry'] == industry]


def get_max_salary(path):
    jobs_list = jobs.read(path)
    salary = set([
        job['max_salary'] for job in jobs_list if job['max_salary'].isdigit()])
    max_salary = max(int(num) for num in salary)
    return max_salary


def get_min_salary(path):
    jobs_list = jobs.read(path)
    salary = set([
        job['min_salary'] for job in jobs_list if job['min_salary'].isdigit()])
    min_salary = min(int(num) for num in salary)
    return min_salary


def matches_salary_range(job, salary):
    try:
        if job['min_salary'] <= int(salary) <= job['max_salary']:
            return True
        elif job['min_salary'] > job['max_salary']:
            raise ValueError
        else:
            return False
    except(KeyError, TypeError, NameError, ValueError):
        raise ValueError


def filter_by_salary_range(jobs, salary):
    list = []
    for job in jobs:
        try:
            result = matches_salary_range(job, salary)
            if result is True:
                list.append(job)
        except ValueError:
            pass
    return list

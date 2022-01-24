import src.jobs


def get_unique_job_types(path):
    # https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
    jobs_in_list = src.jobs.read(path)
    unique_job_type = []
    for job in jobs_in_list:
        if job["job_type"] not in unique_job_type:
            unique_job_type.append(job["job_type"])
    return unique_job_type


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type"""
    jobs_filtered = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filtered.append(job)

    return jobs_filtered


def get_unique_industries(path):
    """Checks all different industries and returns a list of them"""
    jobs_in_list = src.jobs.read(path)
    unique_industries_type = []
    for job in jobs_in_list:
        if (
            job["industry"] not in unique_industries_type
            and job["industry"] != ""
        ):
            unique_industries_type.append(job["industry"])
    return unique_industries_type


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry"""
    industry_filtered = []
    for job in jobs:
        if job["industry"] == industry:
            industry_filtered.append(job)
    return industry_filtered


def get_max_salary(path):
    """Get the maximum salary of all jobs"""
    jobs_in_list = src.jobs.read(path)
    greater_salary = []
    for jobs in jobs_in_list:
        try:
            greater_salary.append(int(jobs["max_salary"]))
        except ValueError:
            pass
    # https://www.programiz.com/python-programming/methods/built-in/max
    return max(greater_salary)


def get_min_salary(path):
    """Get the minimum salary of all jobs"""
    jobs_in_list = src.jobs.read(path)
    minor_salary = []
    for jobs in jobs_in_list:
        try:
            minor_salary.append(int(jobs["min_salary"]))
        except ValueError:
            pass
    return min(minor_salary)


def matches_salary_range(job, salary):

    if "min_salary" not in job or "max_salary" not in job:
        # Raise é pra manualmente "levantar" um erro
        raise (ValueError())
    if (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise (ValueError())
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise (ValueError())
    return int(job["min_salary"]) <= salary <= int(job["max_salary"])

    """Checks if a given salary is in the salary range of a given job
    """


def filter_by_salary_range(jobs, salary):
    good_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                good_jobs.append(job)
        except ValueError:
            pass
    return good_jobs

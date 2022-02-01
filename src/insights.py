from src import jobs


def get_unique_job_types(path):
    jobs_list = jobs.read(path)
    job_types = set()

    for job in jobs_list:
        job_types.add(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []

    for job in jobs:
        if job['job_type'] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs


def get_unique_industries(path):
    jobs_list = jobs.read(path)
    industries = set()

    for job in jobs_list:
        if job["industry"] != "":
            industries.add(job["industry"])

    return industries


def filter_by_industry(jobs, industry):
    filtered_industries = []

    for job in jobs:
        if job['industry'] == industry:
            filtered_industries.append(job)

    return filtered_industries


def get_max_salary(path):
    jobs_list = jobs.read(path)
    max_salary = set()
    for job in jobs_list:
        if job['max_salary'].isnumeric():
            max_salary.add(int(job['max_salary']))
    return max(max_salary)


def get_min_salary(path):
    jobs_list = jobs.read(path)
    min_salary = set()
    for job in jobs_list:
        if job['min_salary'].isnumeric():
            min_salary.add(int(job['min_salary']))
    return min(min_salary)


def matches_salary_range(job, salary):
    try:
        if int(job["min_salary"]) > int(job["max_salary"]):

            raise ValueError

        return int(job["max_salary"]) >= int(salary) >= int(job["min_salary"])
    except Exception:

        raise ValueError


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

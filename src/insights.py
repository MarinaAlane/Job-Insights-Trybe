from src import jobs


def get_unique_job_types(path):
    all_jobs = jobs.read(path)
    job_types = set()
    for job in all_jobs:
        job_types.add(job["job_type"])

    job_types_counter = {job_type: {"jobs": 0} for job_type in job_types}
    for job in all_jobs:
        job_type = job["job_type"]
        job_types_counter[job_type]["jobs"] += 1

    return job_types_counter


def filter_by_job_type(jobs, job_type):
    jobs_filter = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filter.append(job)

    return jobs_filter


def get_unique_industries(path):
    all_jobs = jobs.read(path)
    industries = set()
    for job in all_jobs:
        industries.add(job["industry"])

    industry_counter = {industry: {"jobs": 0} for industry in industries
                        if industry}
    for job in all_jobs:
        industry = job["industry"]
        if industry != '':
            industry_counter[industry]["jobs"] += 1

    return industry_counter


def filter_by_industry(jobs, industry):
    industry_filter = []
    for job in jobs:
        if job["industry"] == industry:
            industry_filter.append(job)

    return industry_filter


def get_max_salary(path):
    all_jobs = jobs.read(path)
    max_salary = set()
    for job in all_jobs:
        if job['max_salary'].isnumeric():
            max_salary.add(int(job['max_salary']))
    return max(max_salary)
    pass


def get_min_salary(path):
    all_jobs = jobs.read(path)
    min_salary = set()
    for job in all_jobs:
        if job['min_salary'].isnumeric():
            min_salary.add(int(job['min_salary']))
    return min(min_salary)
    pass


def matches_salary_range(job, salary):
    if not ('min_salary' in job and 'max_salary' in job):
        raise ValueError
    elif not (isinstance(job['min_salary'], int) and
              isinstance(job['max_salary'], int)):
        raise ValueError
    elif not isinstance(salary, int):
        raise ValueError
    elif job['min_salary'] > job['max_salary']:
        raise ValueError
    else:
        return job['min_salary'] <= salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass
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
    return filtered_jobs

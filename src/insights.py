from src.jobs import read


def get_unique_job_types(path):

    jobs = read(path)
    job_types = set()

    for job in jobs:
        job_types.add(job['job_type'])

    return list(job_types)


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job['job_type'] == job_type]


def get_unique_industries(path):
    jobs_list = read(path)
    industry = set()

    for job in jobs_list:
        if job['industry'] != '':
            industry.add(job['industry'])
    return list(industry)


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job['industry'] == industry]


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = list()
    for job in jobs_list:
        if job['max_salary'].isnumeric():
            max_salary.append(int(job['max_salary']))
    max_salary.sort()
    return max_salary[-1]


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = list()
    for job in jobs_list:
        if job['min_salary'].isnumeric():
            min_salary.append(int(job['min_salary']))
    min_salary.sort()
    return min_salary[0]


def matches_salary_range(job, salary):
    if 'min_salary' not in job.keys() or 'max_salary' not in job.keys():
        raise ValueError('Keys "min_salary" or "max_salary" doesn\'t exists')

    # https://note.nkmk.me/en/python-check-int-float/
    if (
        not isinstance(job['max_salary'], int) or
        not isinstance(job['min_salary'], int)
    ):
        raise ValueError('Keys "min_salary" or "max_salary" not a number')

    if job['min_salary'] > job['max_salary']:
        raise ValueError('"min_salary" is greather than "max_salary"')

    if not isinstance(salary, int):
        raise ValueError('"salary" isn\'t a valid integer')

    return job['min_salary'] <= salary <= job['max_salary']


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

from src.jobs import read


def get_unique_job_types(path):

    return set([item["job_type"] for item in read(path)])


def filter_by_job_type(jobs, job_type):

    return [job for job in jobs if job['job_type'] == job_type]


def get_unique_industries(path):
    # all_ind = read(path)

    # ind = set()
    # for item in all_ind:
    #     industry = item['industry']
    #     if industry != '':
    #         ind.add(item['industry'])
    # print(ind)
    # # return ind
    return {ind["industry"] for ind in read(path) if ind['industry'] != ''}


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    all_salary = read(path)

    max_salary = []
    for item in all_salary:
        if (item["max_salary"] != '' and item['max_salary'] != 'invalid'):
            max_salary.append(int(item['max_salary']))
            max_salary.sort()
    print(max_salary[-1])
    return max_salary[-1]


def get_min_salary(path):
    all_salary = read(path)

    min_salary = []
    for item in all_salary:
        if (item["min_salary"] != '' and item['min_salary'] != 'invalid'):
            min_salary.append(int(item['min_salary']))
            min_salary.sort()
    print(min_salary[0])
    return min_salary[0]


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


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

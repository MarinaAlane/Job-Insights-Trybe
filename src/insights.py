from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    jobs_type_list = []

    for job in jobs_list:
        if job["job_type"] not in jobs_type_list:
            jobs_type_list.append(job["job_type"])
    return jobs_type_list


def filter_by_job_type(jobs, job_type):
    filtered_jobs = [
        job for job in jobs
        if job["job_type"] == job_type
    ]
    return filtered_jobs


def get_unique_industries(path):
    jobs_list = read(path)
    industries_list = []

    for job in jobs_list:
        if job["industry"] != '' and job["industry"] not in industries_list:
            industries_list.append(job["industry"])
    return industries_list


def filter_by_industry(jobs, industry):
    filtered_jobs = [
        job for job in jobs
        if job["industry"] == industry
    ]
    return filtered_jobs


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = 0

    for job in jobs_list:
        try:
            if int(job["max_salary"]) > max_salary:
                max_salary = int(job["max_salary"])
        except ValueError:
            pass
    return max_salary


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = 100000000

    for job in jobs_list:
        try:
            if int(job["min_salary"]) < min_salary:
                min_salary = int(job["min_salary"])
        except ValueError:
            pass
    return min_salary


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise(ValueError())
    elif (type(job["max_salary"]) != int or
          type(job["min_salary"]) != int or
          type(salary) != int):
        raise(ValueError())
    elif job["max_salary"] < job["min_salary"]:
        raise(ValueError())
    return job["max_salary"] >= salary >= job["min_salary"]


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

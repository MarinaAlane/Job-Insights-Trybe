from src.jobs import read


def get_unique_job_types(path):
    list = read(path)
    response = []
    for item in list:
        job_type = item["job_type"]
        if job_type and job_type not in response:
            response.append(job_type)

    return response


def filter_by_job_type(jobs, job_type):
    filtered = [job for job in jobs if job["job_type"] == job_type]

    return filtered


def get_unique_industries(path):
    list = read(path)
    response = []
    for item in list:
        industry = item["industry"]
        if industry and industry not in response:
            response.append(industry)

    return response


def filter_by_industry(jobs, industry):
    filtered = [job for job in jobs if job["industry"] == industry]

    return filtered


def get_max_salary(path):
    list = read(path)
    salaries = []
    for item in list:
        current_salary = item["max_salary"]
        if current_salary.isdigit():
            salaries.append(int(current_salary))

    return max(salaries)


def get_min_salary(path):
    list = read(path)
    salaries = []
    for item in list:
        current_salary = item["min_salary"]
        if current_salary.isdigit():
            salaries.append(int(current_salary))

    return min(salaries)


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError
    elif type(job["min_salary"]) is not int:
        raise ValueError
    elif type(job["max_salary"]) is not int:
        raise ValueError
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError
    elif type(salary) is not int:
        raise ValueError
    elif job["min_salary"] <= salary and salary <= job["max_salary"]:
        return True
    else:
        return False


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

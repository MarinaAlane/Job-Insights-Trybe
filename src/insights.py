from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    # dict_of_unique_jobs = {}
    array_of_types = set()
    for job_type in jobs:
        array_of_types.add(job_type["job_type"])
    return list(array_of_types)


def filter_by_job_type(jobs, job_type):
    filtered_job = filter(lambda job: (job["job_type"] == job_type), jobs)
    return list(filtered_job)


def remove_empty(array):
    for item in array:
        if item != "":
            return True
        else:
            return False


def get_unique_industries(path):
    industries = read(path)
    # dict_of_unique_jobs = {}
    array_of_industries = set()
    for industry in industries:
        array_of_industries.add(industry["industry"])
    # método encontrado em
    # https://www.programiz.com/python-programming/methods/built-in/filter
    filtered_industries = filter(remove_empty, array_of_industries)
    return list(filtered_industries)


def filter_by_industry(jobs, industry):
    filt_ind = filter(lambda x: (x["industry"] == industry), jobs)
    return list(filt_ind)


def get_max_salary(path):
    document = read(path)
    array_of_salaries = set()
    for item in document:
        try:
            array_of_salaries.add(int(item["max_salary"]))
        except ValueError:
            pass

    return max(array_of_salaries)


def get_min_salary(path):
    document = read(path)
    array_of_salaries = set()
    for item in document:
        try:
            array_of_salaries.add(int(item["min_salary"]))
        except ValueError:
            pass

    return min(array_of_salaries)


def filter_salary_validation(job, salary):
    if ("min_salary" not in job or "max_salary" not in job):
        raise ValueError("Whitout min_salary or max_salary")
    if (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError("min_salary or max_salary is not a number")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary is not to be greater than max_salary")

    return True


def matches_salary_range(job, salary):
    filter_salary_validation(job, salary)

    if job["min_salary"] <= salary <= job["max_salary"]:
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

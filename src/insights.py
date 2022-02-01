from src.jobs import read


def filter_dicts_in_list_by_key_value(list_of_dicts, key, value):
    if value == "":
        return list()

    return list(job for job in list_of_dicts if job[key] == value)


def get_distinct_values_by_key(job_list, key):
    results = [job[key] for job in job_list if job[key]]

    return list(set(results))


def get_max_or_min_salary(salaries, comparator, max_or_min):
    for i, salary in enumerate(salaries):
        if i == 0:
            max_or_min = salary
        elif (
            (comparator == '<' and salary.isdigit()) and
            (float(salary) < float(max_or_min))
        ):
            max_or_min = salary
        elif (
            (comparator == '>' and salary.isdigit()) and
            (float(salary) > float(max_or_min))
        ):
            max_or_min = salary

    return float(max_or_min)


def get_unique_job_types(path):
    jobs = read(path)

    return get_distinct_values_by_key(jobs, "job_type")


def filter_by_job_type(jobs, job_type):
    return filter_dicts_in_list_by_key_value(jobs, "job_type", job_type)


def get_unique_industries(path):
    jobs = read(path)

    return get_distinct_values_by_key(jobs, "industry")


def filter_by_industry(jobs, industry):
    return filter_dicts_in_list_by_key_value(jobs, "industry", industry)


def get_max_salary(path):
    jobs = read(path)
    salaries = get_distinct_values_by_key(jobs, "max_salary")
    max_salary = 0.00

    return get_max_or_min_salary(salaries, '>', max_salary)


def get_min_salary(path):
    jobs = read(path)
    salaries = get_distinct_values_by_key(jobs, "min_salary")
    min_salary = 0.00

    return get_max_or_min_salary(salaries, '<', min_salary)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError

    else:
        min_salary = job["min_salary"]
        max_salary = job["max_salary"]

        if (
            type(min_salary) and type(max_salary) not in (int, float)
            or min_salary > max_salary
            or type(salary) is not int
        ):
            raise ValueError

    if (min_salary <= salary) and (max_salary >= salary):
        return True

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

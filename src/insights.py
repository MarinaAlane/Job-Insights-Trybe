from .jobs import read


# Funções criadas como apoio
def get_unique_list(path, key):
    jobs = read(path)
    new_set = set()

    for item in jobs:
        if item[f"{key}"] != "":
            new_set.add(item[f"{key}"])

    return new_set


# Funções padrão do projeto
def get_unique_job_types(path):
    result = get_unique_list(path, "job_type")
    return result


def filter_by_job_type(jobs, job_type):
    jobs_by_type = list()
    for offer in jobs:
        if offer["job_type"] == job_type:
            jobs_by_type.append(offer)

    return jobs_by_type


def get_unique_industries(path):
    result = get_unique_list(path, "industry")
    return result


def filter_by_industry(jobs, industry):
    jobs_by_industry = list()

    for offer in jobs:
        if offer["industry"] == industry:
            jobs_by_industry.append(offer)

    return jobs_by_industry


def get_max_salary(path):
    salaries = get_unique_list(path, "max_salary")
    biggest_salary = 0
    salaries_list = list()
    for salary in salaries:
        if salary.isnumeric():
            salaries_list.append(int(salary))

    for salary in salaries_list:
        if salary >= biggest_salary:
            biggest_salary = salary
    return biggest_salary


def get_min_salary(path):
    salaries = get_unique_list(path, "min_salary")
    salaries_list = list()
    for salary in salaries:
        if salary.isnumeric():
            salaries_list.append(int(salary))

    smallest_salary = salaries_list[0]
    for salary in salaries_list:
        if salary <= smallest_salary:
            smallest_salary = salary
    return smallest_salary


def matches_salary_range(job, salary):

    if not ("max_salary" in job and "min_salary" in job):
        raise ValueError("Keys sohuld be in dict")
    elif (
         type(job["max_salary"]) != int
         or type(job["min_salary"]) != int
         or type(salary) != int
     ):
        raise ValueError("Values should be int")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError(
            "max_salary should be biggest than nim_salary"
          )
    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    filtered_jobs_by_salary_range = list()

    for offer in jobs:
        try:
            is_valid_salary = matches_salary_range(offer, salary)
            if is_valid_salary:
                filtered_jobs_by_salary_range.append(offer)

        except ValueError:
            pass

    return filtered_jobs_by_salary_range

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
    # return []


# python3 -m pytest -k nome_da_func_de_tests
# get_max_salary("/home/silva_enilsom/trybe/projetos/sd-011-project-job-insights/src/jobs.csv")

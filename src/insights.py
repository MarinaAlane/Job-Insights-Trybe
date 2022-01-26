from src.jobs import read


def get_unique_job_types(path):  # ok
    all_jobs_list = read(path)
    unique_job = set()

    for job in all_jobs_list:
        if job["job_type"] is not None:
            unique_job.add(job["job_type"])
    return unique_job


def filter_by_job_type(jobs, job_type):  # ok
    job_list = [job for job in jobs if job["job_type"] == job_type]
    return job_list


def get_unique_industries(path):  # ok
    all_jobs_list = read(path)
    industry_values = set()

    for job in all_jobs_list:
        if job["industry"] != "":
            industry_values.add(job["industry"])
    return industry_values


def filter_by_industry(jobs, industry):  # ok
    job_list = [job for job in jobs if job["industry"] == industry]
    return job_list


def get_max_salary(path):  # ok
    all_jobs_list = read(path)
    all_salaries = set()

    for job in all_jobs_list:
        if job["max_salary"] != "" and job["max_salary"] != "invalid":
            all_salaries.add(int(job["max_salary"]))
    result = sorted(all_salaries)[-1]
    return result


def get_min_salary(path):  # ok
    all_jobs_list = read(path)
    all_salaries = set()

    for job in all_jobs_list:
        if job["min_salary"] != "" and job["min_salary"] != "invalid":
            all_salaries.add(int(job["min_salary"]))
    result = sorted(all_salaries)[0]
    return result


def matches_salary_range(job, salary):  # ok
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError("Chave min_salary ou max_salary não existem")
    elif (
        not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or not isinstance(salary, int)
    ):
        raise ValueError("Não foi passado um valor valido")
    elif job["max_salary"] < job["min_salary"]:
        raise ValueError("max_salary é menor que min_salary")
    elif job["max_salary"] >= salary >= job["min_salary"]:
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

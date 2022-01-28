from src.jobs import read

# import jobs


def get_unique_job_types(path):
    unique_jobs = []
    all_jobs = read(path)
    for row in all_jobs:
        if row["job_type"] not in unique_jobs:
            unique_jobs.append(row["job_type"])
    return unique_jobs


def filter_by_job_type(jobs, job_type):
    jobs_lists = []
    for row in jobs:
        if row["job_type"] == job_type:
            jobs_lists.append(row)
    return jobs_lists


def get_unique_industries(path):
    industries_list = []
    all_jobs = read(path)
    for row in all_jobs:
        if row["industry"] != "" and row["industry"] not in industries_list:
            industries_list.append(row["industry"])

    return industries_list


def filter_by_industry(jobs, industry):
    jobs_lists = []
    for row in jobs:
        if row["industry"] == industry:
            jobs_lists.append(row)
    return jobs_lists


def get_max_salary(path):
    all_salaries = []
    all_jobs = read(path)
    for row in all_jobs:
        if row["max_salary"].isnumeric():
            all_salaries.append(int(row["max_salary"]))
    return max(all_salaries)


def get_min_salary(path):
    all_salaries = []
    all_jobs = read(path)
    for row in all_jobs:
        if row["min_salary"].isnumeric():
            all_salaries.append(int(row["min_salary"]))
    return min(all_salaries)


def matches_salary_range(job, salary):
    if(
        not type(salary) == int or
        not ("max_salary" in job and "min_salary" in job) or
        not type(job["min_salary"]) == int or
        not type(job["max_salary"]) == int or
        job['min_salary'] > job['max_salary']
    ):
        raise ValueError
    else:
        return job["min_salary"] <= salary <= job["max_salary"]


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

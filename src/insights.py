from src import jobs


def get_unique_job_types(path):
    file = jobs.read(path)
    job_types_list = set()
    for row in file:
        if row["job_type"]:
            job_types_list.add(row["job_type"])
    return job_types_list


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    file = jobs.read(path)
    industries_list = set()
    for row in file:
        if row["industry"]:
            industries_list.add(row["industry"])
    return industries_list


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    file = jobs.read(path)
    salary = 0
    for job in file:
        if job["max_salary"].isnumeric() and int(job["max_salary"]) > salary:
            salary = int(job["max_salary"])
    return salary


def get_min_salary(path):
    file = jobs.read(path)
    salary = get_max_salary("src/jobs.csv")
    for job in file:
        if job["min_salary"].isnumeric() and int(job["min_salary"]) < salary:
            salary = int(job["min_salary"])
    return salary


def matches_salary_range(job, salary):
    try:
        if job["min_salary"] < salary < job["max_salary"]:
            return 1
        else:
            return 0
    except ValueError:
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

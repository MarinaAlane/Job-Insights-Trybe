from src.jobs import read


def get_unique_job_types(path):
    get_jobs_data = read(path)
    result = set()
    for get_job_data in get_jobs_data:
        result.add(get_job_data["job_type"])

    return list(result)


def filter_by_job_type(jobs, job_type):
    # para realizar o requisito, utilizei o auxilio de seguinte material:
    # https://www.programiz.com/python-programming/methods/built-in/filter
    filtered_jobs = filter(lambda job: (job["job_type"] == job_type), jobs)

    return list(filtered_jobs)


def get_unique_industries(path):
    get_industries_data = read(path)
    result = []
    for get_industry_data in get_industries_data:
        if get_industry_data["industry"] != "":
            result.append(get_industry_data["industry"])

    return set(result)


def filter_by_industry(jobs, industry):
    f_ind = filter(lambda item: (item["industry"] == industry), jobs)

    return list(f_ind)


def get_max_salary(path):
    get_salaries_data = read(path)
    result = set()

    for get_salary_data in get_salaries_data:
        try:
            result.add(int(get_salary_data["max_salary"]))
        except ValueError:
            pass

    return max(result)


def get_min_salary(path):
    get_salaries_data = read(path)
    result = set()

    for get_salary_data in get_salaries_data:
        try:
            result.add(int(get_salary_data["min_salary"]))
        except ValueError:
            pass

    return min(result)


def matches_salary_range(job, salary):
    if not ("max_salary" in job and "min_salary" in job):
        raise ValueError("salary not found!")
    elif (
        type(job["max_salary"]) != int
        or type(job["min_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError("This values are not compatible with int values")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary is greater than max_salary")
    elif job["min_salary"] <= salary <= job["max_salary"]:

        return True
    return False


def filter_by_salary_range(jobs, salary):
    result = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                result.append(job)
        except ValueError:
            pass

    return result

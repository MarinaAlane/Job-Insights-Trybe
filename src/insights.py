from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    res = list(set(job['job_type'] for job in data))

    return res


def filter_by_job_type(jobs, job_type):
    filter_jobs = list(filter(lambda job: job['job_type'] == job_type, jobs))

    return filter_jobs


def get_unique_industries(path):
    data = read(path)

    all_industries = list(set(job['industry'] for job in data))
    industries = list(filter(None, all_industries))

    return industries


def filter_by_industry(jobs, industry):
    filter_jobs = list(filter(lambda job: job['industry'] == industry, jobs))

    return filter_jobs


def get_max_salary(path):
    data = read(path)

    max_salary_list = filter(
        None,
        list(set(job['max_salary'] for job in data))
    )
    filter_list = filter(
        lambda value: value.isnumeric(),
        list(max_salary_list)
    )

    integer_list = list(map(int, filter_list))
    max_salary = max(integer_list)

    return max_salary


def get_min_salary(path):
    data = read(path)

    min_salary_list = filter(
        None,
        list(set(job['min_salary'] for job in data))
    )
    filter_list = filter(
        lambda value: value.isnumeric(),
        list(min_salary_list)
    )

    integer_list = list(map(int, filter_list))
    min_salary = min(integer_list)

    return min_salary


def matches_salary_range(job, salary):
    if job.get("min_salary") is None or \
            job.get("max_salary") is None or \
            type(job["min_salary"]) != int or \
            type(job["max_salary"]) != int or \
            job["min_salary"] > job["max_salary"] or \
            type(salary) != int:
        raise ValueError()

    if job["min_salary"] <= salary and salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    def returns_false_on_error(func, dict, value):
        try:
            return func(dict, value)
        except Exception:
            return False

    jobs_list = [
        job for job in jobs if returns_false_on_error(
            matches_salary_range, job, salary
        )
    ]

    return jobs_list

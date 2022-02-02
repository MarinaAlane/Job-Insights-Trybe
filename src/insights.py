from src.jobs import read


def filter_dicts_in_list_by_key_value(list_of_dicts, key, value):
    if value == "":
        return list()

    return list(job for job in list_of_dicts if job[key] == value)


def verify_incorrect_values(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        return 'Alguma chaves está ausente nesse dicionário!'

    else:
        min_salary = job["min_salary"]
        max_salary = job["max_salary"]

        if (
            type(min_salary) and type(max_salary) not in (int, float)
            or min_salary > max_salary
            or type(salary) is not int
        ):
            return 'Algum valor está incorreto ou desbalanceado!'


def get_distinct_values_by_key(job_list, key):
    results = [job[key] for job in job_list if job[key]]

    return list(set(results))


def get_max_or_min_salary(salaries, max_or_min):
    result = 0.00

    for salary in salaries:
        try:
            salary = float(salary)
            if max_or_min == 'min':
                result = salary if not result or salary < result else result

            else:
                result = salary if not result or salary > result else result
        except ValueError:
            continue
    return result


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

    return get_max_or_min_salary(salaries, 'max')


def get_min_salary(path):
    jobs = read(path)
    salaries = get_distinct_values_by_key(jobs, "min_salary")

    return get_max_or_min_salary(salaries, 'min')


def matches_salary_range(job, salary):
    error = verify_incorrect_values(job, salary)

    if error:
        raise ValueError

    if job['min_salary'] <= salary <= job['max_salary']:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    jobs_in_salary_range = []
    for job in jobs:
        try:
            salary_range = matches_salary_range(job, salary)

            if salary_range:
                jobs_in_salary_range.append(job)
        except ValueError:
            continue
    return jobs_in_salary_range

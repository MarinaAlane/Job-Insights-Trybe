def get_unique_job_types(path):
    from src.jobs import read

    content = read(path)

    types = set()  # Conjuto de Jobs
    # Referencia do comando Pass:
    # www.delftstack.com/pt/howto/python/python-pass/#:text=A%20instru%C3%A7%C3%A3o%20pass%20%C3%A9%20usada,que%20o%20programa%20fa%C3%A7a%20nada.
    for job in content:
        if job["job_type"] in types:
            pass
        else:
            types.add(job["job_type"])
    return types


def filter_by_job_type(jobs, job_type):
    filtered_job_types = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_job_types.append(job)
    return filtered_job_types


def get_unique_industries(path):
    from src.jobs import read

    content = read(path)

    industries = set()

    for job in content:
        if job["industry"] == "":  # Excluindo registros vazios
            pass
        else:
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    filtered_industry = []

    for job in jobs:
        if job["industry"] == industry:
            filtered_industry.append(job)
    return filtered_industry


def get_max_salary(path):
    from src.jobs import read

    content = read(path)

    get_salaries = set()

    for job in content:
        if job["max_salary"]:
            try:
                get_salaries.add(int(job["max_salary"]))
            except ValueError:
                continue  # gerando exceção para valor não-inteiro
    return max(get_salaries)


def get_min_salary(path):
    from src.jobs import read

    content = read(path)

    get_salaries = set()

    for job in content:
        if job["min_salary"]:
            try:
                get_salaries.add(int(job["min_salary"]))
            except ValueError:
                continue
    return min(get_salaries)


def matches_salary_range(job, salary):
    try:
        if int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError  # laçando as exceções no Error para facilitar
        return int(job["max_salary"]) >= int(salary) >= int(job["min_salary"])
    except Exception:
        raise ValueError  # laçando as exceções no Error para facilitar


def filter_by_salary_range(jobs, salary):
    jobs_filtered = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_filtered.append(job)
        except ValueError:
            continue
    return jobs_filtered

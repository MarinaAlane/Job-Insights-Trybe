from src import jobs


def get_unique_job_types(path):
    all_jobs = jobs.read(path)
    job_types = list()
    for job in all_jobs:
        if job["job_type"] in job_types:
            pass
        else:
            job_types.append(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    filter_job_type = list(
        filter(lambda jobs_type: jobs_type["job_type"] == job_type, jobs)
    )

    return filter_job_type


# para os requisitos de filtro usei esse link como referencia ao usar o filter:
# https://www.digitalocean.com/community/tutorials/how-to-use-the-python-filter-function-pt
# pesquisa realizada em 28/01/22


def get_unique_industries(path):
    all_jobs = jobs.read(path)
    job_industries_list = list()
    for job in all_jobs:
        if job["industry"] == "" or job["industry"] in job_industries_list:
            pass
        else:
            job_industries_list.append(job["industry"])

    return job_industries_list


def filter_by_industry(jobs, industry):
    filter_job_industry = filter(lambda job: job["industry"] == industry, jobs)

    return list(filter_job_industry)


def get_max_salary(path):
    all_jobs = jobs.read(path)
    higher_salary = 0
    for job in all_jobs:
        if job["max_salary"] == "" or not job["max_salary"].isnumeric():
            continue
        elif int(job["max_salary"]) > higher_salary:
            higher_salary = int(job["max_salary"])
    return higher_salary


def get_min_salary(path):
    all_jobs = jobs.read(path)
    lower_salary = 0
    for job in all_jobs:
        if job["min_salary"] == "" or not job["min_salary"].isnumeric():
            continue
        elif lower_salary == 0 or int(job["min_salary"]) < lower_salary:
            lower_salary = int(job["min_salary"])
    return lower_salary
    pass


# Para o requisito 8 e 9, um colega de trabalho me direcionou na resolução e
# indicou pesquisar sobre erros (excessões).
# Todas as pesquisas foram realizadas em 29/01/22
# https://docs.python.org/pt-br/3/tutorial/errors.html
# https://www.geeksforgeeks.org/python-raise-keyword/

# Pesquisas para o resquisito 9 (valueError, except)
# https://www.w3schools.com/python/python_try_except.asp
# https://www.datacamp.com/community/tutorials/exception-handling-python?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1001566&gclid=Cj0KCQiAxc6PBhCEARIsAH8Hff32VfizUsGEOsRAIS4vRYNl5lLiMJfSXkfTPRhR6GXK_TtJ0fM5TbkaArSFEALw_wcB


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Values not found")
    elif (
        not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or not isinstance(salary, int)
    ):
        raise ValueError("Invalid values")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary higher than max_salary")
    elif salary < job["min_salary"] or salary > job["max_salary"]:
        return False
    else:
        return True


def filter_by_salary_range(jobs, salary):
    salary_range = list()

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salary_range.append(job)
        except ValueError:
            pass
    return salary_range

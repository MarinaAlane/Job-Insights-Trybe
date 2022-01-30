from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    jobs_type = []
    # Se não tiver a linha job_type dentro do array vazio, é adicionado ao
    # array

    for row in data:
        if row["job_type"] not in jobs_type:
            jobs_type.append(row["job_type"])
    return jobs_type


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    # Verifica o job_types do jobs, e adiciona na lista.
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):

    content = read(path)
    industries = []
    # A cada linha verifica se não existe 'industry' dentro do array e
    # se não é vazio então coloca dentro do array industries
    for row in content:
        if row["industry"] not in industries and row["industry"] != "":
            industries.append(row["industry"])
    return industries


def filter_by_industry(jobs, industry):
    filtered_industries = []
    # Verifica o job_types do jobs, e adiciona na lista.
    for job in jobs:
        if job["industry"] == industry:
            filtered_industries.append(job)
    return filtered_industries


def get_max_salary(path):
    content = read(path)
    salaries = []
    # A cada linha verifica se o max_salary é um dígito,
    # e adiciona na lista salaries.
    # colocando como inteiro e retorna a lista
    for row in content:
        if row["max_salary"].isdigit():
            salaries.append(int(row["max_salary"]))
    return max(salaries)


def get_min_salary(path):

    content = read(path)
    salaries = []
    # A cada linha verifica se o min_salary é um dígito, e adiciona
    # na lista salaries, colocando como inteiro e retorna a lista
    for row in content:
        if row["min_salary"].isdigit():
            salaries.append(int(row["min_salary"]))
    return min(salaries)


def matches_salary_range(job, salary):
    # Se em job não tiver as chaves max_salary ou min_salary.
    # Retorna mensagem de erro.
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError("Chaves são necessárias")
    elif (
        # Verifica se o salary, max_salary, min_salary
        # Se são do tipo inteiro, caso contrário dispara um erro.
        type(job["max_salary"]) != int
        or type(job["min_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError("As chaves não são números")
    elif job["max_salary"] < job["min_salary"]:
        raise ValueError("Salário Inválido")
    else:
        pass
        # Se todas as condições anteriores forem falsas, a função
        # vai retornar o salário menores ou iguais ao salario min
        # e os salários maiores ou iguais ao salário maximo.
    return salary >= job["min_salary"] and salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    list_of_salaries = []
    # Coloca na lista list_of_salaries tudo que a função
    # anterior retornar de exceção
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_of_salaries.append(job)
        except ValueError:
            pass

    return list_of_salaries

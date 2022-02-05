from src import jobs


def get_unique_job_types(path):
    conjunto = set()
    arquivo_csv = jobs.read(path)

    for linha in arquivo_csv:
        conjunto.add(linha["job_type"])

    return conjunto


def filter_by_job_type(jobs, job_type):
    modalidades = []

    for contrato in jobs:
        if contrato['job_type'] == job_type:
            modalidades.append(contrato)

    return modalidades


def get_unique_industries(path):
    conjunto = set()
    arquivo_csv = jobs.read(path)

    for linha in arquivo_csv:
        conjunto.add(linha["industry"])

    conjunto = list(filter(None, conjunto))
    return conjunto


def filter_by_industry(jobs, industry):
    categoria = []

    for industrias in jobs:
        if industrias['industry'] == industry:
            categoria.append(industrias)

    return categoria


def get_max_salary(path):
    conjunto = set()
    arquivo_csv = jobs.read(path)

    for linha in arquivo_csv:
        if linha["max_salary"].isnumeric():
            conjunto.add(int(linha["max_salary"]))

    maior_salario = max(conjunto)
    return maior_salario


def get_min_salary(path):
    conjunto = set()
    arquivo_csv = jobs.read(path)

    for linha in arquivo_csv:
        if linha["min_salary"].isnumeric():
            conjunto.add(int(linha["min_salary"]))

    menor_salario = min(conjunto)
    return menor_salario


def matches_salary_range(job, salary):
    maior_salario = 'max_salary'
    menor_salario = 'min_salary'

    if (
        type(salary) != int
        or menor_salario not in job
        or maior_salario not in job
        or type(job[menor_salario]) != int
        or type(job[maior_salario]) != int
        or job[menor_salario] > job[maior_salario]
    ):
        raise ValueError("Value Error")

    salary = (job[maior_salario] >= salary >= job[menor_salario])

    return salary


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

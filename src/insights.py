def get_unique_job_types(path):
    # Requisito 2

    from src.jobs import read

    content = read(path)

    # Criei um conjunto, onde não haverão itens repetidos.
    types = set()

    # Se o item já estiver no conjunto ignore a condição.
    # Se o item não estiver no conjunto será adicionado.
    # Referencia do comando pass abaixo:
    # https://docs.python.org/pt-br/3/tutorial/controlflow.html#:~:text=%3E%3E%3E%20while%20True%3A%0A...-,pass,-%23%20Busy%2Dwait%20for

    for job in content:
        if job["job_type"] in types:
            pass
        else:
            types.add(job["job_type"])
    return types


def filter_by_job_type(jobs, job_type):
    # Requisito 6

    filtered_job_types = []

    # Primeiro iterei sobre a lista de empregos.
    # Depois fiz um filtro do tipo do emprego, pelo passado por parâmetro.
    # Se a condição for verdadeira retorne o emprego filtrado.
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_job_types.append(job)
    return filtered_job_types


def get_unique_industries(path):
    # Requisito 3

    from src.jobs import read

    content = read(path)

    # Criei um conjunto, onde não haverão itens repetidos.
    industries = set()

    # Se o nome da industria estiver vazio nada acontece.
    # Se houver uma industria irá adicioná-la ao conjunto industries
    for job in content:
        if job["industry"] == "":
            pass
        else:
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    # Requisito 7

    filtered_industry = []

    # Primeiro iterei sobre a lista de empregos.
    # Depois fiz um filtro de indústrias, pela passada por parâmetro.
    # Se a condição for verdadeira retorne a industria filtrada.
    for job in jobs:
        if job["industry"] == industry:
            filtered_industry.append(job)
    return filtered_industry


def get_max_salary(path):
    # Requisito 4

    from src.jobs import read

    content = read(path)

    # Utilizo do conjunto para evitar valores repetidos.
    get_salaries = set()

    # Adiciono os valores já inteiros, se sua coluna for max_salary.
    # Senão lanço uma exceção, pois não são valores inteiros.
    # O comando continue apenas passa para a proxima iteração do laço.
    # Por fim capturo o maior valor com a função max().
    for job in content:
        if job["max_salary"]:
            try:
                get_salaries.add(int(job["max_salary"]))
            except ValueError:
                continue
    return max(get_salaries)


def get_min_salary(path):
    # Requisito 5

    from src.jobs import read

    content = read(path)

    # Utilizo do conjunto para evitar valores repetidos.
    get_salaries = set()

    # Adiciono os valores já inteiros, se sua coluna for min_salary.
    # Senão lanço uma exceção, pois não são valores inteiros.
    # O comando continue apenas passa para a proxima iteração do laço.
    # Por fim capturo o menor valor com a função min().
    for job in content:
        if job["min_salary"]:
            try:
                get_salaries.add(int(job["min_salary"]))
            except ValueError:
                continue
    return min(get_salaries)


def matches_salary_range(job, salary):
    # Requisito 08
    # Ajuda do Rahel e Rodrigo no plantão para...
    # ...reduzir a complexidade das condições da minha função.

    # O retorno da linha 127 é implicito, ele avalia a condição...
    # ...e retorna True se verdadeira, e False se falsa.

    # Como as exceções do requisito são iguais, criei um...
    # ...lançamento de erro genérico retornando ValueError.
    try:
        if int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError
        return int(job["max_salary"]) >= int(salary) >= int(job["min_salary"])
    except Exception:
        raise ValueError


def filter_by_salary_range(jobs, salary):
    # Requisito 9

    # escolhi fazer com lista pois é ordenada e mutável.
    jobs_filtered = []

    # Se o emprego se encaixa na faixa salarial adiciono na lista.
    # Senão lanço um ValueError e continuo a condição.
    # Por fim, retorno a lista.
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_filtered.append(job)
        except ValueError:
            continue
    return jobs_filtered

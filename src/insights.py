from src.jobs import read


def get_unique_job_types(path):
    file = read(path)
    jobs_types = set()  # 1
    for index in file:
        if index["job_type"] != "":  # 2
            jobs_types.add(index["job_type"])  # 3
    return jobs_types


# get_unique_job_types('jobs.csv')

"""
-> Função - get_unique_job_types()
1 - Quando se usa o set() nao incluimos os repetidos
    (tentei com job_types = [] + appende pegou todos repetido)
2 - pegamamos todos os [job types] dentro de cada iteração no index
3 - Adiciona cada job_type distintos dentro do conjunto jobs_types
"""

# ---------------------------------------------------------------------------------


def filter_by_job_type(jobs, job_type):
    jobs_filter = []
    for index in jobs:
        if job_type == index["job_type"]:  # 1
            jobs_filter.append(index)  # 2
    return jobs_filter


'''
-> Função - filter_by_job_type()
1 - Se o parametro job_type for igual a iteração com o ["job_type"]
2 - Adiciona a iteração do index no jobs a lista jobs_filter
'''

# ---------------------------------------------------------------------------------


def get_unique_industries(path):
    file = read(path)
    distinct_industries = set()  # 1
    for index in file:
        if index["industry"] != "":  # 2
            distinct_industries.add(index["industry"])  # 3
    # print(distinct_industries)

    return distinct_industries


# get_unique_industries('jobs.csv')

"""
-> Função - get_unique_industries()
1 - Quando se usa o set() nao incluimos os repetidos
(tentei com job_types = [] + appende pegou todos repetido)
2 - Linha 8 - pegamamos todos os [job types] dentro de cada iteração no index
3 - Adiciona cada job_type distintos dentro do conjunto jobs_types
"""
# ---------------------------------------------------------------------------------


def filter_by_industry(jobs, industry):
    jobs_filter = []
    for index in jobs:
        if industry == index["industry"]:  # 1
            jobs_filter.append(index)  # 2
    return jobs_filter


'''
-> Função - filter_by_industry()
1 - Se o parametro industry for igual a iteração com o ["industry"]
2 - Adiciona a iteração do index no jobs a lista jobs_filter
'''

# ---------------------------------------------------------------------------------


def get_max_salary(path):
    file = read(path)
    max_salary = []
    for index in file:
        if index["max_salary"].isdigit():  # 1
            salary_info = int(index["max_salary"])  # 2
            max_salary.append(salary_info)  # 3
    # print(max(max_salary))
    return(max(max_salary))  # 4


# get_max_salary("jobs.csv")

"""
-> Função - get_max_salary()
1 - Verifica se o index[max_salary] é um digito
2 - Transforma as informaçõs em int caso ele não seja esse tipo de dado
3 - Adiciona o valor na lista max_salary
4 - Retorna o maior salario usando a função Max
"""

# ---------------------------------------------------------------------------------


def get_min_salary(path):
    file = read(path)
    min_salary = []
    for index in file:
        if index["min_salary"].isdigit():  # 1
            salary_info = int(index["min_salary"])  # 2
            min_salary.append(salary_info)  # 3
    # print(min(min_salary))
    return(min(min_salary))  # 4


# get_min_salary("jobs.csv")

"""
-> Função - get_min_salary()
1 - Verifica se o index[min_salary] é um digito
2 - Transforma as informaçõs em int caso ele não seja esse tipo de dado
3 - Adiciona o valor na lista min_salary
4 - Retorna o maior salario usando a função Min
"""

# ---------------------------------------------------------------------------------


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:  # 1
        raise ValueError
    if (
        not type(job["max_salary"]) == int
        or
        not type(job["min_salary"]) == int
        or
        not type(salary) == int
    ):  # 2
        raise ValueError
    elif job["min_salary"] > job["max_salary"]:  # 3
        raise ValueError
    if job["min_salary"] <= salary <= job["max_salary"]:  # 4
        return True
    return False


'''
-> Função - matches_salary_range()
1 - Se nao houver dentro de job os "max_salary ou min_salary envia um erro"
2 - Caso esses valores nao sejam inteiros envia um erro
3 - Se por acaso o min_salary for menor que o max_salary envia um KeyError
4 - Caso o salario esteja entre o min_salary e o max_salary retorna
    True senão retorna False
'''

# ---------------------------------------------------------------------------------


def filter_by_salary_range(jobs, salary):
    jobs_filter = []
    for index in jobs:
        try:
            if matches_salary_range(index, salary):  # 1
                jobs_filter.append(index)  # 2
        except ValueError:  # 3
            continue
    return jobs_filter  # 4


'''
-> Função - filter_by_salary_range()
1 - Tenta verificar se chamando a função matches_salary_range()
    enviando os parametros ele retorna True
2 - Caso seja True inclui o valor iterado dentro da lista jobs_filter
3 - Se algo ocorra errado emite um erro
4 - Retorna a lista com o salarios filtrados
'''


# ---------------------------------------------------------------------------------

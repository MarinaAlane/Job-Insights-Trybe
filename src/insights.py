from src import jobs


def get_unique_job_types(path):
    jobs_list = jobs.read(path)
    job_types = []
    for job in jobs_list:
        job_types.append(job['job_type'])
    return list(set(job_types))


# importo da pasta SRC o jobs.
# a função deve retornar uma lista dos tipos de contratação
# existentes em forma de lista.
# jobs.read() chama a função read de jobs, abre o arquivo, carrega a info
# e a atribui em jobs_list. Cria-se uma variavél para armazenar os tipos de
# contrato. E faz-se o forIn adicionando todas as contratações ao job_types
# Posteriormente utilizo-me de set, pois o mesmo filtra elementos repetidos.
# e retorno a lista.


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job['job_type'] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


# a função filter_by_job_type tem dois parametros, sendo o primeiro
# uma lista de jobs contendo id e tipo de trabalho(o tipo de trabalho se
# repete). O forIN em jobs tem como filtro o job_type. Portanto toda
# vez que o job_type da lista for igual ao job_type do parametro o
# job será adicionado na filtered_jobs, com seus ids e job_types


def get_unique_industries(path):
    jobs_list = jobs.read(path)
    ind_types = []
    for job in jobs_list:
        if job['industry']:
            ind_types.append(job['industry'])
    return list(set(ind_types))


# a função get_unique_industries le o arquivo CSV
# e coloca na variável ind_types os tipos de industrias encontradas
# na lista. O if questiona se o job[industry] é vazio ou nao e se nao
# adiciona-o na vriavel, retornando os tipos cadastrados.

def filter_by_industry(jobs, industry):
    filtered_inds = []
    print('ooooooooo', jobs, 'hhhhhhhhhh', industry)
    for job in jobs:
        if job['industry'] == industry:
            filtered_inds.append(job)
    return filtered_inds


# a função filter_by_industry tem dois parametros, sendo o primeiro
# uma lista de jobs contendo id e tipo de industria(o tipo de industria se
# repete). O forIN em jobs tem como filtro o industry. Portanto toda
# vez que a industria da lista for igual ao industry do parametro o
# job será adicionado na filtered_jobs, com seus ids e industrias


def get_max_salary(path):
    jobs_list = jobs.read(path)
    salaries = []
    for job in jobs_list:
        if job['max_salary']:
            salaries.append(int(job['max_salary']))
    greater_salary = max(salaries)
    return greater_salary


def get_min_salary(path):
    jobs_list = jobs.read(path)
    salaries = []
    for job in jobs_list:
        if job['min_salary']:
            salaries.append(int(job['min_salary']))
    less_salary = min(salaries)
    return less_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
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

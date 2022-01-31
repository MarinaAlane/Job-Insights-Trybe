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
        if job['max_salary'].isdigit():
            salaries.append(int(job['max_salary']))
    greater_salary = max(salaries)
    return greater_salary


# os instrutores Rodrigo Curvo e Isaac Prates, e tbm o colega Hugo Somers
# me ajudaram a resolver o problema que tive com a transformação de dados
# em int, uma vez que existiam células vazias e células com caracteres
# diferentes de numeros.

# a função get_max_salary le o arquivo CSV, abre uma variavel salaries
# faz se um forIn em jobs e verifica-se se o dado é um digito, se for
# faz o append em salaries. Seleciona o salário máximo e o retorna.


def get_min_salary(path):
    jobs_list = jobs.read(path)
    salaries = []
    for job in jobs_list:
        if job['min_salary'].isdigit():
            salaries.append(int(job['min_salary']))
    less_salary = min(salaries)
    return less_salary


# a função get_min_salary le o arquivo CSV, abre uma variavel salaries
# faz se um forIn em jobs e verifica-se se o dado é um digito, se for
# faz o append em salaries. Seleciona o salário mínimo e o retorna.


def matches_salary_range(job, salary):
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError('min_salary/max_salary are necessary')
    elif (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError('min_salary/max_salary needs to be a number')
    elif job['min_salary'] > job['max_salary']:
        raise ValueError('min_salary is greater than max_salary!')
    elif salary < job['min_salary'] or salary > job['max_salary']:
        return False
    else:
        return True

# a função matches_salary_range indica a faixa salarial em que a
# pessoa necessita filtrar os trabalhos.
# a primeira linha verifica se foram informados min_salary ou max_salary.
# se houver um erro o raise será acionado e um erro será lançado.
# Se o primeiro if for satisfeito deve-se verificar se os dados em max_salary e
# min_salary são múmeros.
# sendo também satisfeitos, verifica-se se o min_salary é realmente menor que
# max_salary
# E tbm se o salario está entre min e max, se todas informações forem
# corretas a função retorna true. Se não retorna false, ou os erros;


def filter_by_salary_range(jobs, salary):
    filtered_salary_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_salary_range.append(job)
        except ValueError:
            pass
    return filtered_salary_range

# a função filter_by_salary_range é um filtro que se utiliza da
# funçao matches_salary_range para fazer validações. Então estando todas
# as validações corretas ele retorna os jobs que satisfazem as regras de
# negócio.

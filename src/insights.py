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
2 - Linha 8 - pegamamos todos os [job types] dentro de cada iteração no index
3 - Adiciona cada job_type distintos dentro do conjunto jobs_types
"""

# ---------------------------------------------------------------------------------


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []

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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []

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
1 - Verifica se o index[min_salary] existe
2 - Transforma as informaçõs em int caso ele não seja esse tipo de dado
3 - Adiciona o valor na lista min_salary
4 - Retorna o maior salario usando a função Min
"""

# ---------------------------------------------------------------------------------


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

# ---------------------------------------------------------------------------------


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

    # ---------------------------------------------------------------------------------

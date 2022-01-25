from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    jobs_types = set()
    for job in jobs_list:
        jobs_types.add(job["job_type"])
    return jobs_types


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


def get_unique_industries(path):
    fileContent = read(path)
    industries = set()
    for industry in fileContent:
        if industry["industry"] != '':
            industries.add(industry["industry"])
    return industries


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


def get_max_salary(path):
    fileContent = read(path)  # leio o arquivo
    max_salary = 0  # crio uma variavel p/ armazenar maior salario
    for salary in fileContent:  # pra cada salary na minha lista lida
        payment = salary["max_salary"]
        # defino como payment o valor da chave 'max salary' do item
        if payment != '' and payment != 'invalid':
            # se payment for = a vazio ou invalido não entra na equação
            if int(payment) > int(max_salary):
                # se o int de payment é maior que o valor armazenado em max_sal
                max_salary = payment  # add na coleção
                # altero a variavel para o novo valor
    return int(max_salary)


def get_min_salary(path):
    fileContent = read(path)  # leio o arquivo
    min_salary = []  # crio uma variavel p/ armazenar salarios
    for salary in fileContent:  # pra cada salary na minha lista lida
        payment = salary["min_salary"]
        # defino como payment o valor da chave 'min salary' do item
        if payment != '' and payment != 'invalid':
            # se payment for = a vazio ou invalido não entra na equação
            min_salary.append(int(payment))
            # adiciona a lista o valor INT de payment
    return min(min_salary)
    # função min que retorna o menor valor do iteravel

# Referencia para utilziação da função min:
# https://www.w3schools.com/python/ref_func_min.asp


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

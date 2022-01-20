# from jobs import read

from src.jobs import read

# path_csv = "/home/monts/Documents/trybe/
# projetos/sd-011-project-job-insights/src/jobs.csv"


def get_unique_job_types(path):  # & done
    table = read(path)
    dict_with_all_jobs_types = dict()
    for row in table:
        if row["job_type"] in dict_with_all_jobs_types:
            dict_with_all_jobs_types[row["job_type"]] += 1
        else:
            dict_with_all_jobs_types[row["job_type"]] = 1
    # .. source: https://www.tutorialspoint.com/
    # .. How-to-convert-Python-Dictionary-to-a-list
    list_of_jobs = list(dict_with_all_jobs_types.keys())
    return list_of_jobs


def filter_by_job_type(jobs, job_type):  # & done
    filtered_jobs = []
    for row in jobs:
        if job_type == row["job_type"]:
            filtered_jobs.append(row)
    return filtered_jobs


# print(filter_by_job_type(path_csv, "PART_TIME"))


def get_unique_industries(path):  # & done
    table = read(path)
    dict_with_all_industries = dict()
    for row in table:
        if row["industry"] in dict_with_all_industries:
            dict_with_all_industries[row["industry"]] += 1
        elif len(row["industry"]) > 0:
            dict_with_all_industries[row["industry"]] = 1
    list_of_industries = list(dict_with_all_industries.keys())
    return list_of_industries


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


def get_max_salary(path):  # & done
    table = read(path)
    all_salaries = []
    for row in table:
        if row["max_salary"].isnumeric():
            all_salaries.append(int(row["max_salary"]))
    all_salaries.sort(reverse=True)
    biggest_salary = all_salaries[0]
    return biggest_salary


def get_min_salary(path):  # & done
    table = read(path)
    all_salaries = []
    for row in table:
        if row["min_salary"].isnumeric():
            all_salaries.append(int(row["min_salary"]))
    all_salaries.sort()
    lowest_salary = all_salaries[0]
    return lowest_salary


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

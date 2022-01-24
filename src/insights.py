from src import jobs
# import jobs


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    file_content = jobs.read(path)
    job_types_set = {
        content['job_type'] for content in file_content
    }
    job_types_list = list(job_types_set)
    return job_types_list


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
    filtered_jobs_list = [
        job for job in jobs if job['job_type'] == job_type
    ]
    return filtered_jobs_list


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    file_content = jobs.read(path)
    industries_set = {
        content['industry']
        for content in file_content if content['industry'] != ''
    }
    industries_list = list(industries_set)
    return industries_list


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
    filtered_jobs_list = [
        job for job in jobs if job['industry'] == industry
    ]
    return filtered_jobs_list


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    file_content = jobs.read(path)
    max_salaries_set = {
        int(content['max_salary'], 10)
        for content in file_content if content['max_salary'].isdecimal()
    }
    highest_max_salary = max(max_salaries_set)
    return highest_max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    file_content = jobs.read(path)
    min_salaries_set = {
        int(content['min_salary'], 10)
        for content in file_content if content['min_salary'].isdecimal()
    }
    lowest_min_salary = min(min_salaries_set)
    return lowest_min_salary


def check_job_and_salary(job, salary):
    return (
        'min_salary' not in job
        or 'max_salary' not in job
        or type(job['max_salary']) is not int
        or type(job['min_salary']) is not int
        or job['max_salary'] < job['min_salary']
        or (type(salary) is not int)
    )


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
    is_not_valid = check_job_and_salary(job, salary)
    if is_not_valid is True:
        raise ValueError('Invalid value')
    return job['min_salary'] <= salary <= job['max_salary']


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
    filtered_jobs_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary) is True:
                filtered_jobs_list.append(job)
        except ValueError:
            pass
    return filtered_jobs_list


if __name__ == "__main__":
    # print(get_unique_job_types('./src/jobs.csv'))
    # print(get_unique_industries('./src/jobs.csv'))
    # print(get_max_salary('./src/jobs.csv'))
    # print(get_min_salary('./src/jobs.csv'))
    # print(filter_by_job_type(
    #     [
    #         {"id": 1, "job_type": "PART_TIME"},
    #         {"id": 2, "job_type": "PART_TIME"},
    #         {"id": 3, "job_type": "OTHER"},
    #         {"id": 4, "job_type": "OTHER"},
    #         {"id": 5, "job_type": "FULL_TIME"},
    #         {"id": 6, "job_type": "FULL_TIME"},
    #         {"id": 7, "job_type": "CONTRACTOR"},
    #         {"id": 8, "job_type": "CONTRACTOR"},
    #         {"id": 9, "job_type": "TEMPORARY"},
    #         {"id": 10, "job_type": "TEMPORARY"},
    #         {"id": 11, "job_type": "INTERN"},
    #         {"id": 12, "job_type": "INTERN"},
    #     ], "PART_TIME"
    # ))
    # print(filter_by_industry(
    #     [
    #         {"id": 1, "industry": "agriculture"},
    #         {"id": 2, "industry": "agriculture"},
    #         {"id": 3, "industry": "solar energy"},
    #         {"id": 4, "industry": "solar energy"},
    #         {"id": 5, "industry": "bank"},
    #         {"id": 6, "industry": "bank"},
    #         {"id": 7, "industry": "mechanical engineering"},
    #         {"id": 8, "industry": "mechanical engineering"},
    #         {"id": 9, "industry": "translation"},
    #         {"id": 10, "industry": "translation"},
    #         {"id": 11, "industry": "finances"},
    #         {"id": 12, "industry": "finances"},
    #     ], "agriculture"
    # ))
    # print(matches_salary_range({
    #     "max_salary": 1500, "min_salary": 100
    # }, 1000))
    # print(filter_by_salary_range(
    #     [
    #         {"max_salary": 0, "min_salary": 10},
    #         {"max_salary": 10, "min_salary": 100},
    #         {"max_salary": 10000, "min_salary": 200},
    #         {"max_salary": 15000, "min_salary": 0},
    #         {"max_salary": 1500, "min_salary": 0},
    #         {"max_salary": -1, "min_salary": 10},
    #     ], 1000
    # ))
    pass

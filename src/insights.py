from src.jobs import read


def get_unique_job_types(path):
    table = read(path)
    dict_with_all_jobs_types = dict()
    for row in table:
        dict_with_all_jobs_types[row["job_type"]] = 1
    # .. source: https://www.tutorialspoint.com/
    # .. How-to-convert-Python-Dictionary-to-a-list
    list_of_jobs = list(dict_with_all_jobs_types.keys())
    return list_of_jobs


"""
    It's possible to reduce complexity using set() insted of dict()
    would be necessary to transforme it into a list and as a note
    dict don't need to use this verification about if the key already exists
    (already fixed)
"""


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for row in jobs:
        if job_type == row["job_type"]:
            filtered_jobs.append(row)
    return filtered_jobs


def get_unique_industries(path):
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
    filtered_industry = []
    for row in jobs:
        if industry == row["industry"]:
            filtered_industry.append(row)
    return filtered_industry


def get_max_salary(path):
    table = read(path)
    all_salaries = []
    for row in table:
        if row["max_salary"].isnumeric():
            all_salaries.append(int(row["max_salary"]))
    all_salaries.sort(reverse=True)
    biggest_salary = all_salaries[0]
    return biggest_salary


def get_min_salary(path):
    table = read(path)
    all_salaries = []
    for row in table:
        if row["min_salary"].isnumeric():
            all_salaries.append(int(row["min_salary"]))
    all_salaries.sort()
    lowest_salary = all_salaries[0]
    return lowest_salary


"""
    Python has the philosophy not to force things so as another way to
    do this would be using try and except - A more pythonic way to do
"""


def verify_valid_params(min, max, salary):
    if min == "empty" or max == "empty":
        raise ValueError(
            "`job['min_salary']` or `job['max_salary']` doesn't exists"
        )
    elif not str(min).isnumeric() or not str(max).isnumeric():
        raise ValueError(
            "`job['min_salary']` or `job['max_salary']` aren't valid integers"
        )
    elif min > max:
        raise ValueError(
            "`job['min_salary']` is greather than `job['max_salary']`"
        )
    # ..source: https://www.codegrepper.com/code-examples/shell/
    # ..  python+isnumeric+negative+numbers
    elif not str(salary).lstrip("-").isnumeric():
        raise ValueError("`salary` isn't a valid integer")


def matches_salary_range(job, salary):
    # ..source: https://stackoverflow.com/questions/6130768/
    # .. return-none-if-dictionary-key-is-not-available
    min = job.get("min_salary", "empty")
    max = job.get("max_salary", "empty")
    try:
        verify_valid_params(min, max, salary)
    except ValueError:
        raise ValueError("Oops! Try again...")
    else:
        if int(min) <= int(salary) <= int(max):
            return True
        else:
            return False


"""
    this one is good, instead of use if's could be create little functions
    that would return true or false
    as used here:
    https://github.com/tryber/sd-011-project-job-insights/blob/luiz-wendel-job-insights-project/src/insights.py
    this is way better to reduce it's complexity
"""


def filter_by_salary_range(jobs, salary):
    list_of_matched_jobs = list()
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_of_matched_jobs.append(job)
        except ValueError:
            continue
    return list_of_matched_jobs

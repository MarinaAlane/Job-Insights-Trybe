def is_valid_job(job, salary=0):
    if (
        not type(job["min_salary"]) is int
        or not type(job["max_salary"]) is int
        or not type(salary) is int
        or job["min_salary"] >= job["max_salary"]
    ):
        return False

    return True

def verify_key(job):
    if not ("min_salary" in job and "max_salary" in job):
        return True


def verify_key_number(job):
    if (type(job["min_salary"]) != int or type(job["max_salary"]) != int):
        return True


def verify_correct_order(job):
    if (job["min_salary"] > job["max_salary"]):
        return True


def verify_salary_number(salary):
    if (type(salary) != int):
        return True


def all_validations(job, salary):
    if (
      verify_key(job) or
      verify_key_number(job) or
      verify_correct_order(job) or
      verify_salary_number(salary)
    ):
        raise ValueError("Error validations")

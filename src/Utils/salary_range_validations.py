''' Para verificar a existencia de uma determinada key em um dict,
consultei este topico no StackOverFlow
stackoverflow.com/
questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary'''


def verify_if_key_exists(job):
    if not ("min_salary" in job and "max_salary" in job):
        return True


def verify_if_keys_show_empty_string(job):
    if job["min_salary"] == "" and job["max_salary"] == "":
        return True


def verify_if_keys_are_type_number(job):
    if type(job["min_salary"]) != int and type(job["max_salary"]) != int:
        return True


def verify_if_min_salary_is_greather_than_max_salary(job):
    if job["min_salary"] > job["max_salary"]:
        return True


def verify_if_salary_is_of_type_int(salary):
    if type(salary) != int:
        return True


def salary_range_validation(job, salary):
    if (
        verify_if_key_exists(job) or
        verify_if_keys_show_empty_string(job) or
        verify_if_keys_are_type_number(job) or
        verify_if_min_salary_is_greather_than_max_salary(job) or
        verify_if_salary_is_of_type_int(salary)
    ):
        raise ValueError("Invalid value of salary")

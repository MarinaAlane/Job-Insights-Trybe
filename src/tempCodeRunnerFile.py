data_job = read(path)
    salary = set()
    for job in data_job:
        if job["max_salary"].isnumeric():
            salary.add(int(job["max_salary"]))

    return max(salary)
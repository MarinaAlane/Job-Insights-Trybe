def get_salary_list(job_list, salary_key):
    jobs_salary = [int(job[salary_key])
                   for job in job_list
                   if job[salary_key].strip() != ''
                   and job[salary_key] != 'invalid']

    return jobs_salary

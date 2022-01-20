def filter_by_column(jobs, job_type, column):
    filtered_jobs = []
    for job in jobs:
        if job[column] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs
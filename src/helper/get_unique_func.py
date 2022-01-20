def get_unique_list_from_column(jobs_list, column):
    unique_list = set()
    for job in jobs_list:
        if job[column] != '':
            unique_list.add(job[column])
    return unique_list

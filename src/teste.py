from jobs import read


# def get_unique_job_types(path):
#     file = read(path)
#     jobs_types = set()
#     for index in file:
#         if index["job_type"] != "":
#             jobs_types.add(index["job_type"])
#     return jobs_types


# get_unique_job_types('jobs.csv')


def get_unique_industries(path):
    file = read(path)
    distinct_industries = set()
    for index in file:
        if index["industry"] != "":
            distinct_industries.add(index["industry"])
    print(distinct_industries)

    return distinct_industries


get_unique_industries('jobs.csv')

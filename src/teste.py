# from jobs import read


# def get_max_salary(path):
#     file = read(path)
#     max_salary = []
#     for index in file:
#         if index["max_salary"]:
#             salary_info = int(index["max_salary"])
#             max_salary.append(salary_info)
#     print(max(max_salary))
#     return(max(max_salary))


# get_max_salary("jobs.csv")


# def get_max_salary(path):
#     jobs_info = read(path)
#     max_salary = []
#     for job in jobs_info:
#         if job["max_salary"]:
#             try:
#                 salary = int(job["max_salary"])
#             except ValueError:
#                 continue
#             max_salary.append(salary)
#     print(max(max_salary))
#     return max(max_salary)


# get_max_salary("jobs.csv")


# def get_min_salary(path):
#     """Get the minimum salary of all jobs

#     Must call `read`

#     Parameters
#     ----------
#     path : str
#         Must be passed to `read`

#     Returns
#     -------
#     int
#         The minimum salary paid out of all job opportunities
#     """
#     pass

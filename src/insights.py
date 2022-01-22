from jobs import read


def get_unique_job_types(path):
    listJobs = read(path)
    setJobs = set()
    for job in listJobs:
        setJobs.add(job["job_type"])
    return setJobs


def filter_by_job_type(jobs, job_type):
    return [j for j in jobs if j["job_type"] == job_type]


def get_unique_industries(path):
    listJobs = read(path)
    setJobs = set()
    for job in listJobs:
        if "industry" in job:
            if job["industry"] != "":
                setJobs.add(job["industry"])
    return setJobs


def filter_by_industry(jobs, industry):
    return [j for j in jobs if j["industry"] == industry]


def get_max_salary(path):
    listJobs = read(path)
    value = 0
    for job in listJobs:
        if job["max_salary"] != "":
            if int(job["max_salary"]) > value:
                value = int(job["max_salary"])
    return value


def get_min_salary(path):
    listJobs = read(path)
    value = get_max_salary(path)
    for job in listJobs:
        if job["min_salary"] != "":
            if int(job["min_salary"]) < value:
                value = int(job["min_salary"])
    return value


def matches_salary_range(job, salary):
    value = 0
    return value


print(matches_salary_range("src/jobs.csv"))


def filter_by_salary_range(jobs, salary):
    return []

from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as jobs_file:
        #     header, *jobs_list = csv.reader(jobs_file)
        #     jobs_list_dict = []
        #     for job in jobs_list:
        #         job_obj = {item: job[header.index(item)] for item in header}
        #         jobs_list_dict.append(job_obj)

        # return jobs_list_dict
        all_jobs = []
        jobs_list = csv.DictReader(jobs_file, delimiter=",", quotechar='"')
        for job in jobs_list:
            all_jobs.append(job)

    return all_jobs

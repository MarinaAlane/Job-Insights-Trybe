import pytest
from src.sorting import sort_by

fake_jobs = [
    {"min_salary": 20, "max_salary": 500, "date_posted": "2020-07-08"},
    {"min_salary": 30, "max_salary": 50, "date_posted": "2020-07-10"},
    {"min_salary": 10, "max_salary": 40, "date_posted": "2020-07-09"},
]

wrong_fake_jobs = [
    {"min_salary": "t", "max_salary": 500, "date_posted": "2020-07-08"},
    {"min_salary": 30, "max_salary": 50, "date_posted": "2020-07-10"},
    {"min_salary": 10, "max_salary": 40, "date_posted": "2020-07-09"},
]

jobs_sort_by_max_salary = [fake_jobs[0], fake_jobs[1], fake_jobs[2]]
jobs_sort_by_min_salary = [fake_jobs[2], fake_jobs[0], fake_jobs[1]]
jobs_sort_by_date = [fake_jobs[1], fake_jobs[2], fake_jobs[0]]

keys = ["min_salary", "max_salary", "date_posted"]
sorts = [jobs_sort_by_min_salary, jobs_sort_by_max_salary, jobs_sort_by_date]


def test_sort_by_criteria():
    with pytest.raises((KeyError, TypeError, ValueError)):
        sort_by(wrong_fake_jobs, "min_salary")

    with pytest.raises(
            (KeyError, TypeError, ValueError),
            match="invalid sorting criteria:"):
        sort_by(fake_jobs, "batata")

    # for idx_key, key in enumerate(keys):
    #     response = sort_by(fake_jobs, key)
    #     for idx_resp, resp in enumerate(response):
    #         assert resp == sorts[idx_key][idx_resp]

    print(sort_by(fake_jobs, "min_salary"))

    assert sort_by(fake_jobs, "min_salary") == jobs_sort_by_min_salary
    # assert sort_by(fake_jobs, "max_salary") == jobs_sort_by_max_salary
    # assert sort_by(fake_jobs, "date_posted") == jobs_sort_by_date

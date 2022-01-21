from src.sorting import sort_by
import pytest


jobs = [
    {"min_salary": 5000, "max_salary": 10000, "date_posted": "2022-12-12"},
    {"min_salary": 1000, "max_salary": 20000, "date_posted": "2022-11-11"},
    {"min_salary": 10000, "max_salary": 25000, "date_posted": "2022-10-10"},
    ]
jobs_by_min_salary = [
    {"min_salary": 1000, "max_salary": 20000, "date_posted": "2022-11-11"},
    {"min_salary": 5000, "max_salary": 10000, "date_posted": "2022-12-12"},
    {"min_salary": 10000, "max_salary": 25000, "date_posted": "2022-10-10"},
    ]
jobs_by_max_salary = [
    {"min_salary": 10000, "max_salary": 25000, "date_posted": "2022-10-10"},
    {"min_salary": 1000, "max_salary": 20000, "date_posted": "2022-11-11"},
    {"min_salary": 5000, "max_salary": 10000, "date_posted": "2022-12-12"},
    ]

jobs_by_date_posted = [
    {"min_salary": 5000, "max_salary": 10000, "date_posted": "2022-12-12"},
    {"min_salary": 1000, "max_salary": 20000, "date_posted": "2022-11-11"},
    {"min_salary": 10000, "max_salary": 25000, "date_posted": "2022-10-10"},
    ]


def test_sort_by_criteria_worng_criteria():
    jobs_copy = jobs.copy()
    sort_by(jobs_copy, "min_salary") 
    assert jobs_copy == jobs_by_min_salary

    jobs_copy = jobs.copy()
    sort_by(jobs_copy, "max_salary") 
    assert jobs_copy == jobs_by_max_salary

    jobs_copy = jobs.copy()
    sort_by(jobs_copy, "date_posted") 
    assert jobs_copy == jobs_by_date_posted

    with pytest.raises(ValueError, match="invalid sorting criteria: wrong"):
        sort_by(jobs,  "wrong")


# def test_sort_by_criteria_order():
#     print(jobs)
#     print(sort_by(jobs, "min_salary"))
#     print(sort_by(jobs, "max_salary"))
#     print(sort_by(jobs, "date_posted"))
#     assert sort_by(jobs, "min_salary") == jobs_by_min_salary
#     assert sort_by(jobs, "max_salary") == jobs_by_max_salary
#     assert sort_by(jobs, "date_posted") == jobs_by_date_posted

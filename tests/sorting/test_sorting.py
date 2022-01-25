from src.sorting import sort_by
import pytest


jobs = [
    {"min_salary": 500, "max_salary": 3000, "date_posted": "2023-04-03"},
    {"min_salary": 1000, "max_salary": 4500, "date_posted": "2024-04-03"},
    {"min_salary": 2000, "max_salary": 5000, "date_posted": "2022-07-11"},
]

jobs_min_salary = [
    {"min_salary": 1050, "max_salary": 3050, "date_posted": "2022-12-08"},
    {"min_salary": 2300, "max_salary": 4587, "date_posted": "2022-12-09"},
    {"min_salary": 13253, "max_salary": 24656, "date_posted": "2023-11-12"},
]

jobs_max_salary = [
    {"min_salary": 9567, "max_salary": 16453, "date_posted": "2023-01-07"},
    {"min_salary": 234, "max_salary": 445, "date_posted": "2024-02-08"},
    {"min_salary": 5534, "max_salary": 7654, "date_posted": "2025-03-09"},
]

jobs_date_posted = [
    {"min_salary": 3000, "max_salary": 30000, "date_posted": "2023-15-03"},
    {"min_salary": 2000, "max_salary": 20000, "date_posted": "2024-14-04"},
    {"min_salary": 8000, "max_salary": 80000, "date_posted": "2025-13-05"},
]


def test_sort_by_criteria():
    jobs_copy = jobs.copy()
    sort_by(jobs_copy, "min_salary")
    assert jobs_copy == jobs_min_salary

    jobs_copy = jobs.copy()
    sort_by(jobs_copy, "max_salary")
    assert jobs_copy == jobs_max_salary

    jobs_copy = jobs.copy()
    sort_by(jobs_copy, "date_posted")
    assert jobs_copy == jobs_date_posted

    with pytest.raises(ValueError):
        sort_by(jobs, "Error")

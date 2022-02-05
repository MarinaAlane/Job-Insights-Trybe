from src.sorting import sort_by

# import pytest

jobs_example = [
    {"min_salary": 3000, "max_salary": 7000, "date_posted": "1995-11-15"},
    {"min_salary": 1000, "max_salary": 5000, "date_posted": "2020-05-08"},
    {"min_salary": 1500, "max_salary": 8000, "date_posted": "2018-12-03"},
]


def test_sort_by_criteria():
    sort_by(jobs_example, "min_salary")
    assert jobs_example == [
        {"min_salary": 1000, "max_salary": 5000, "date_posted": "2020-05-08"},
        {"min_salary": 1500, "max_salary": 8000, "date_posted": "2018-12-03"},
        {"min_salary": 3000, "max_salary": 7000, "date_posted": "1995-11-15"},
    ]

    sort_by(jobs_example, "max_salary")
    assert jobs_example == [
        {"min_salary": 1500, "max_salary": 8000, "date_posted": "2018-12-03"},
        {"min_salary": 3000, "max_salary": 7000, "date_posted": "1995-11-15"},
        {"min_salary": 1000, "max_salary": 5000, "date_posted": "2020-05-08"},
    ]

    sort_by(jobs_example, "date_posted")
    assert jobs_example == [
        {"min_salary": 1000, "max_salary": 5000, "date_posted": "2020-05-08"},
        {"min_salary": 1500, "max_salary": 8000, "date_posted": "2018-12-03"},
        {"min_salary": 3000, "max_salary": 7000, "date_posted": "1995-11-15"},
    ]

import pytest
from src.sorting import sort_by

jobs = [
    {"min_salary": 3500, "max_salary": 7000, "date_posted": "2018-06-20"},
    {"min_salary": 1000, "max_salary": 2100, "date_posted": "2015-02-17"},
    {"min_salary": 1470, "max_salary": 2419, "date_posted": "2012-06-25"},
]


def test_sort_by_criteria():
    with pytest.raises(TypeError):
        sort_by(jobs, "fail", "try")

    sort_by(jobs, "date_posted")
    assert jobs == [
        {"min_salary": 3500, "max_salary": 7000, "date_posted": "2018-06-20"},
        {"min_salary": 1000, "max_salary": 2100, "date_posted": "2015-02-17"},
        {"min_salary": 1470, "max_salary": 2419, "date_posted": "2012-06-25"},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == [
        {"min_salary": 1000, "max_salary": 2100, "date_posted": "2015-02-17"},
        {"min_salary": 1470, "max_salary": 2419, "date_posted": "2012-06-25"},
        {"min_salary": 3500, "max_salary": 7000, "date_posted": "2018-06-20"},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == [
        {"min_salary": 3500, "max_salary": 7000, "date_posted": "2018-06-20"},
        {"min_salary": 1470, "max_salary": 2419, "date_posted": "2012-06-25"},
        {"min_salary": 1000, "max_salary": 2100, "date_posted": "2015-02-17"},
    ]

import pytest
from src.sorting import sort_by


jobs = [
    {"min_salary": 4000, "max_salary": 5000, "date_posted": "2022-01-24"},
    {"min_salary": 3000, "max_salary": 4000, "date_posted": "2022-01-25"},
    {"min_salary": 5000, "max_salary": 7000, "date_posted": "2022-01-26"},
]

min_order = [
    {"min_salary": 3000, "max_salary": 4000, "date_posted": "2022-01-25"},
    {"min_salary": 4000, "max_salary": 5000, "date_posted": "2022-01-24"},
    {"min_salary": 5000, "max_salary": 7000, "date_posted": "2022-01-26"},
]

max_order = [
    {"min_salary": 5000, "max_salary": 7000, "date_posted": "2022-01-26"},
    {"min_salary": 4000, "max_salary": 5000, "date_posted": "2022-01-24"},
    {"min_salary": 3000, "max_salary": 4000, "date_posted": "2022-01-25"},
]

date_order = [
    {"min_salary": 5000, "max_salary": 7000, "date_posted": "2022-01-26"},
    {"min_salary": 3000, "max_salary": 4000, "date_posted": "2022-01-25"},
    {"min_salary": 4000, "max_salary": 5000, "date_posted": "2022-01-24"},
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == min_order
    sort_by(jobs, "max_salary")
    assert jobs == max_order
    sort_by(jobs, "date_posted")
    assert jobs == date_order
    with pytest.raises(ValueError):
        sort_by(jobs, "AAAAAAAAA")

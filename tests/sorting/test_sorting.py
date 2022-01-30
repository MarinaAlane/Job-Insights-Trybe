import pytest
from src.sorting import sort_by

jobs = [
    {"min_salary": 2100, "max_salary": 4500, "date_posted": "2020-03-29"},
    {"min_salary": 1220, "max_salary": 7000, "date_posted": "2020-09-14"},
    {"min_salary": 3050, "max_salary": 4800, "date_posted": "2020-02-05"},
]

min_salary = [
    {"min_salary": 1220, "max_salary": 7000, "date_posted": "2020-09-14"},
    {"min_salary": 2100, "max_salary": 4500, "date_posted": "2020-03-29"},
    {"min_salary": 3050, "max_salary": 4800, "date_posted": "2020-02-05"},
]

max_salary = [
    {"min_salary": 1220, "max_salary": 7000, "date_posted": "2020-09-14"},
    {"min_salary": 3050, "max_salary": 4800, "date_posted": "2020-02-05"},
    {"min_salary": 2100, "max_salary": 4500, "date_posted": "2020-03-29"},
]

date_posted = [
    {"min_salary": 1220, "max_salary": 7000, "date_posted": "2020-09-14"},
    {"min_salary": 2100, "max_salary": 4500, "date_posted": "2020-03-29"},
    {"min_salary": 3050, "max_salary": 4800, "date_posted": "2020-02-05"},
]


def test_sort_by_criteria():
    with pytest.raises(TypeError):
        sort_by(jobs, "criteria", "criteria2")

    sort_by(jobs, "min_salary")
    assert jobs == min_salary

    sort_by(jobs, "max_salary")
    assert jobs == max_salary

    sort_by(jobs, "date_posted")
    assert jobs == date_posted

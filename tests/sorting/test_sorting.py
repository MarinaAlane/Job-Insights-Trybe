import pytest
from src.sorting import sort_by

jobs_mocked = [
    {"min_salary": 3, "max_salary": 4, "date_posted": "2022-03-01"},
    {"min_salary": 2, "max_salary": 3, "date_posted": "2022-02-01"},
    {"min_salary": 1, "max_salary": 2, "date_posted": "2022-01-01"},
    {"min_salary": 5, "max_salary": 6, "date_posted": "2022-05-01"},
    {"min_salary": 4, "max_salary": 5, "date_posted": "2022-04-01"},
]

by_max_salary = [
    {"min_salary": 5, "max_salary": 6, "date_posted": "2022-05-01"},
    {"min_salary": 4, "max_salary": 5, "date_posted": "2022-04-01"},
    {"min_salary": 3, "max_salary": 4, "date_posted": "2022-03-01"},
    {"min_salary": 2, "max_salary": 3, "date_posted": "2022-02-01"},
    {"min_salary": 1, "max_salary": 2, "date_posted": "2022-01-01"},
]

by_min_salary = [
    {"min_salary": 1, "max_salary": 2, "date_posted": "2022-01-01"},
    {"min_salary": 2, "max_salary": 3, "date_posted": "2022-02-01"},
    {"min_salary": 3, "max_salary": 4, "date_posted": "2022-03-01"},
    {"min_salary": 4, "max_salary": 5, "date_posted": "2022-04-01"},
    {"min_salary": 5, "max_salary": 6, "date_posted": "2022-05-01"},
]

by_date_posted = [
    {"min_salary": 5, "max_salary": 6, "date_posted": "2022-05-01"},
    {"min_salary": 4, "max_salary": 5, "date_posted": "2022-04-01"},
    {"min_salary": 3, "max_salary": 4, "date_posted": "2022-03-01"},
    {"min_salary": 2, "max_salary": 3, "date_posted": "2022-02-01"},
    {"min_salary": 1, "max_salary": 2, "date_posted": "2022-01-01"},
]


def test_sort_by_criteria():
    sort_by(jobs_mocked, "max_salary")
    assert jobs_mocked == by_max_salary

    sort_by(jobs_mocked, "min_salary")
    assert jobs_mocked == by_min_salary

    sort_by(jobs_mocked, "date_posted")
    assert jobs_mocked == by_date_posted

    with pytest.raises(ValueError):
        sort_by(jobs_mocked, "None")

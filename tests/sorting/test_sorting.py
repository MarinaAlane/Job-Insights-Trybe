import pytest
from src.sorting import sort_by

jobs_mocked = [
    {"min_salary": 2, "max_salary": 4, "date_posted": "2020-03-01"},
    {"min_salary": 1, "max_salary": 6, "date_posted": "2020-01-01"},
    {"min_salary": 3, "max_salary": 5, "date_posted": "2020-02-01"},
]


def test_sort_by_criteria():
    pass
    sort_by(jobs_mocked, "min_salary")
    assert jobs_mocked == [
        {"min_salary": 1, "max_salary": 6, "date_posted": "2020-01-01"},
        {"min_salary": 2, "max_salary": 4, "date_posted": "2020-03-01"},
        {"min_salary": 3, "max_salary": 5, "date_posted": "2020-02-01"},
    ]

    sort_by(jobs_mocked, "max_salary")
    assert jobs_mocked == [
        {"min_salary": 1, "max_salary": 6, "date_posted": "2020-01-01"},
        {"min_salary": 3, "max_salary": 5, "date_posted": "2020-02-01"},
        {"min_salary": 2, "max_salary": 4, "date_posted": "2020-03-01"},
    ]

    sort_by(jobs_mocked, "date_posted")
    assert jobs_mocked == [
        {"min_salary": 2, "max_salary": 4, "date_posted": "2020-03-01"},
        {"min_salary": 3, "max_salary": 5, "date_posted": "2020-02-01"},
        {"min_salary": 1, "max_salary": 6, "date_posted": "2020-01-01"},
    ]

    with pytest.raises(ValueError):
        sort_by(jobs_mocked, "invalid_criteria")

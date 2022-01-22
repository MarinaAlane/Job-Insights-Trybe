import pytest
from src.sorting import sort_by

fake_jobs = [
    {"min_salary": 10, "max_salary": 20, "date_posted": "2022-01-22"},
    {"min_salary": 20, "max_salary": 30, "date_posted": "2022-01-21"},
    {"min_salary": 30, "max_salary": 40, "date_posted": "2022-01-20"},
]


def test_sort_by_criteria():
    pass
    sort_by(fake_jobs, "min_salary")
    assert fake_jobs == [
        {"min_salary": 10, "max_salary": 20, "date_posted": "2022-01-22"},
        {"min_salary": 20, "max_salary": 30, "date_posted": "2022-01-21"},
        {"min_salary": 30, "max_salary": 40, "date_posted": "2022-01-20"},
    ]

    sort_by(fake_jobs, "max_salary")
    assert fake_jobs == [
        {"min_salary": 30, "max_salary": 40, "date_posted": "2022-01-20"},
        {"min_salary": 20, "max_salary": 30, "date_posted": "2022-01-21"},
        {"min_salary": 10, "max_salary": 20, "date_posted": "2022-01-22"},
    ]

    sort_by(fake_jobs, "date_posted")
    assert fake_jobs == [
        {"min_salary": 10, "max_salary": 20, "date_posted": "2022-01-22"},
        {"min_salary": 20, "max_salary": 30, "date_posted": "2022-01-21"},
        {"min_salary": 30, "max_salary": 40, "date_posted": "2022-01-20"},
    ]

    with pytest.raises(ValueError):
        sort_by(fake_jobs, "invalid_criteria")

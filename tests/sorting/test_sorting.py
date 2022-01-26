import pytest
from src.sorting import sort_by

mocks = [
    {"min_salary": 1000, "max_salary": 3500, "date_posted": "2022-01-01"},
    {"min_salary": 3000, "max_salary": 3000, "date_posted": "2022-03-03"},
    {"min_salary": 2000, "max_salary": 2000, "date_posted": "2022-02-02"},
]


def test_sort_by_criteria():
    sort_by(mocks, "max_salary")
    assert mocks == [
        {"min_salary": 1000, "max_salary": 3500, "date_posted": "2022-01-01"},
        {"min_salary": 3000, "max_salary": 3000, "date_posted": "2022-03-03"},
        {"min_salary": 2000, "max_salary": 2000, "date_posted": "2022-02-02"},
    ]

    sort_by(mocks, "min_salary")
    assert mocks == [
        {"min_salary": 1000, "max_salary": 3500, "date_posted": "2022-01-01"},
        {"min_salary": 2000, "max_salary": 2000, "date_posted": "2022-02-02"},
        {"min_salary": 3000, "max_salary": 3000, "date_posted": "2022-03-03"},
    ]

    sort_by(mocks, "date_posted")
    assert mocks == [
        {"min_salary": 3000, "max_salary": 3000, "date_posted": "2022-03-03"},
        {"min_salary": 2000, "max_salary": 2000, "date_posted": "2022-02-02"},
        {"min_salary": 1000, "max_salary": 3500, "date_posted": "2022-01-01"},
    ]

    with pytest.raises(ValueError):
        sort_by(mocks, "param")

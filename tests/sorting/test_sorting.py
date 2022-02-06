import pytest
from src.sorting import sort_by

jobs = [
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2022-01-01"},
    {"min_salary": 2000, "max_salary": 4000, "date_posted": "2022-02-02"},
]

min = [
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2022-01-01"},
    {"min_salary": 2000, "max_salary": 4000, "date_posted": "2022-02-02"},
]

max = [
    {"min_salary": 2000, "max_salary": 4000, "date_posted": "2022-02-02"},
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2022-01-01"},
]

date = [
    {"min_salary": 2000, "max_salary": 4000, "date_posted": "2022-02-02"},
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2022-01-01"},
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == min

    sort_by(jobs, "max_salary")
    assert jobs == max

    sort_by(jobs, "date_posted")
    assert jobs == date

    with pytest.raises(ValueError):
        sort_by(jobs, "invalid_data")
    pass

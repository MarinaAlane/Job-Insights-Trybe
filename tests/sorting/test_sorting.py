import pytest
from src.sorting import sort_by


@pytest.fixture()
def jobs():
    return [
        {"min_salary": 3500, "max_salary": 5000, "date_posted": "2022-01-01"},
        {"min_salary": 3600, "max_salary": 6000, "date_posted": "2022-01-02"},
        {"min_salary": 3700, "max_salary": 6500, "date_posted": "2022-01-03"},
    ]


jobs_min_salary = [
    {"min_salary": 3500, "max_salary": 5000, "date_posted": "2022-01-01"},
    {"min_salary": 3600, "max_salary": 6000, "date_posted": "2022-01-02"},
    {"min_salary": 3700, "max_salary": 6500, "date_posted": "2022-01-03"},
]

jobs_max_salary = [
    {"min_salary": 3700, "max_salary": 6500, "date_posted": "2022-01-03"},
    {"min_salary": 3600, "max_salary": 6000, "date_posted": "2022-01-02"},
    {"min_salary": 3500, "max_salary": 5000, "date_posted": "2022-01-01"},
]

jobs_date_posted = [
    {"min_salary": 3700, "max_salary": 6500, "date_posted": "2022-01-03"},
    {"min_salary": 3600, "max_salary": 6000, "date_posted": "2022-01-02"},
    {"min_salary": 3500, "max_salary": 5000, "date_posted": "2022-01-01"},
]


def test_sort_by_criteria(jobs):
    sort_by(jobs, "min_salary")
    assert jobs == jobs_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == jobs_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == jobs_date_posted

    with pytest.raises(ValueError):
        sort_by(jobs, "salary")

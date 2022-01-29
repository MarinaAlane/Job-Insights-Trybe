import pytest
from src.sorting import sort_by


# @pytest.fixture
def jobs_list():
    return [
        {"min_salary": 2000, "max_salary": 3000, "data-posted": "2022-01-27"},
        {"min_salary": 1100, "max_salary": 2500, "data-posted": "2022-02-27"},
        {"min_salary": 2100, "max_salary": 2200, "data-posted": "2022-01-01"},
    ]


ordered_by_date = [
    {"min_salary": 2100, "max_salary": 2200, "data-posted": "2022-01-01"},
    {"min_salary": 2000, "max_salary": 3000, "data-posted": "2022-01-27"},
    {"min_salary": 1100, "max_salary": 2500, "data-posted": "2022-02-27"},
]

ordered_by_max_salary = [
    {"min_salary": 2000, "max_salary": 3000, "data-posted": "2022-01-27"},
    {"min_salary": 1100, "max_salary": 2500, "data-posted": "2022-02-27"},
    {"min_salary": 2100, "max_salary": 2200, "data-posted": "2022-01-01"},
]

ordered_by_min_salary = [
    {"min_salary": 1100, "max_salary": 2500, "data-posted": "2022-02-27"},
    {"min_salary": 2000, "max_salary": 3000, "data-posted": "2022-01-27"},
    {"min_salary": 2100, "max_salary": 2200, "data-posted": "2022-01-01"},
]


def test_sort_by_criteria():
    jobs = jobs_list()
    sort_by(jobs, "date_posted")
    assert jobs == ordered_by_date

    jobs = jobs_list()
    sort_by(jobs, "max_salary")
    assert jobs == ordered_by_max_salary

    jobs = jobs_list()
    sort_by(jobs, "min_salary")
    assert jobs == ordered_by_min_salary

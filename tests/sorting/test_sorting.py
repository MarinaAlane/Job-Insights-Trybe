import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {"min_salary": 3500, "max_salary": 7500, "date_posted": "2022-02-17"},
        {"min_salary": 6500, "max_salary": 15000, "date_posted": "2022-05-12"},
        {"min_salary": 5500, "max_salary": 10000, "date_posted": "2022-01-05"},
    ]


def test_sort_by_criteria(jobs):
    order_by_min_salary = [
        {"min_salary": 3500, "max_salary": 7500, "date_posted": "2022-02-17"},
        {"min_salary": 5500, "max_salary": 10000, "date_posted": "2022-01-05"},
        {"min_salary": 6500, "max_salary": 15000, "date_posted": "2022-05-12"},
    ]

    jobs_copy = jobs.copy()
    sort_by(jobs_copy, "min_salary")
    assert jobs_copy == order_by_min_salary

    order_by_max_salary = [
        {"min_salary": 6500, "max_salary": 15000, "date_posted": "2022-05-12"},
        {"min_salary": 5500, "max_salary": 10000, "date_posted": "2022-01-05"},
        {"min_salary": 3500, "max_salary": 7500, "date_posted": "2022-02-17"},
    ]

    jobs_copy = jobs.copy()
    sort_by(jobs_copy, "max_salary")
    assert jobs_copy == order_by_max_salary

    order_by_date_posted = [
        {"min_salary": 6500, "max_salary": 15000, "date_posted": "2022-05-12"},
        {"min_salary": 3500, "max_salary": 7500, "date_posted": "2022-02-17"},
        {"min_salary": 5500, "max_salary": 10000, "date_posted": "2022-01-05"},
    ]

    jobs_copy = jobs.copy()
    sort_by(jobs_copy, "date_posted")
    assert jobs_copy == order_by_date_posted

    invalid_criteria = "invalid_criteria"
    with pytest.raises(
        ValueError, match=f"invalid sorting criteria: {invalid_criteria}"
    ):
        jobs_copy = jobs.copy()
        sort_by(jobs_copy, invalid_criteria)

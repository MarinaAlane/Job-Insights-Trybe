import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {"min_salary": 500, "max_salary": 10000, "date_posted": "2022-06-27"},
        {"min_salary": 1500, "max_salary": 25000, "date_posted": "2022-09-13"},
        {"min_salary": 1000, "max_salary": 15000, "date_posted": "2022-07-05"},
    ]


def test_sort_by_criteria(jobs):
    order_by_min_salary = [
        {"min_salary": 500, "max_salary": 10000, "date_posted": "2022-06-27"},
        {"min_salary": 1000, "max_salary": 15000, "date_posted": "2022-07-05"},
        {"min_salary": 1500, "max_salary": 25000, "date_posted": "2022-09-13"},
    ]
    jobs_min = jobs.copy()
    sort_by(jobs_min, "min_salary")
    assert jobs_min == order_by_min_salary

    order_by_max_salary = [
        {"min_salary": 1500, "max_salary": 25000, "date_posted": "2022-09-13"},
        {"min_salary": 1000, "max_salary": 15000, "date_posted": "2022-07-05"},
        {"min_salary": 500, "max_salary": 10000, "date_posted": "2022-06-27"},
    ]
    jobs_max = jobs.copy()
    sort_by(jobs_max, "max_salary")
    assert jobs_max == order_by_max_salary

    order_by_date_posted = [
        {"min_salary": 1500, "max_salary": 25000, "date_posted": "2022-09-13"},
        {"min_salary": 1000, "max_salary": 15000, "date_posted": "2022-07-05"},
        {"min_salary": 500, "max_salary": 10000, "date_posted": "2022-06-27"},
    ]
    jobs_date = jobs.copy()
    sort_by(jobs_date, "date_posted")
    assert jobs_date == order_by_date_posted

    not_a_criteria = "not_a_criteria"
    with pytest.raises(
        ValueError, match="invalid sorting criteria: not_a_criteria"
    ):
        sort_by(jobs, not_a_criteria)

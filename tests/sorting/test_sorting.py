import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {"min_salary": 0, "max_salary": 500, "date_posted": "2020-05-08"},
        {"min_salary": 2000, "max_salary": 25000, "date_posted": "2020-07-23"},
        {"min_salary": 1100, "max_salary": 7500, "date_posted": "2020-03-27"},
    ]


def test_sort_by_criteria(jobs):
    order_min_salary = [
        {"min_salary": 0, "max_salary": 500, "date_posted": "2020-05-08"},
        {"min_salary": 1100, "max_salary": 7500, "date_posted": "2020-03-27"},
        {"min_salary": 2000, "max_salary": 25000, "date_posted": "2020-07-23"},
    ]
    order_max_salary = [
        {"min_salary": 2000, "max_salary": 25000, "date_posted": "2020-07-23"},
        {"min_salary": 1100, "max_salary": 7500, "date_posted": "2020-03-27"},
        {"min_salary": 0, "max_salary": 500, "date_posted": "2020-05-08"},
    ]
    order_date_posted = [
        {"min_salary": 2000, "max_salary": 25000, "date_posted": "2020-07-23"},
        {"min_salary": 0, "max_salary": 500, "date_posted": "2020-05-08"},
        {"min_salary": 1100, "max_salary": 7500, "date_posted": "2020-03-27"},
    ]

    jobs_copy = jobs.copy()
    sort_by(jobs_copy, "min_salary")
    assert jobs_copy == order_min_salary

    jobs_copy = jobs.copy()
    sort_by(jobs_copy, "max_salary")
    assert jobs_copy == order_max_salary

    jobs_copy = jobs.copy()
    sort_by(jobs_copy, "date_posted")
    assert jobs_copy == order_date_posted

    invalid_criterias = ["industry", "job_type"]

    for invalid_criteria in invalid_criterias:
        with pytest.raises(
            ValueError, match=f"invalid sorting criteria: {invalid_criteria}"
        ):
            jobs_copy = jobs.copy()
            sort_by(jobs_copy, invalid_criteria)

import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {"max_salary": 20000, "min_salary": 1200, "date_posted": "2001-10-02"},
        {"max_salary": 15000, "min_salary": 5000, "date_posted": "2001-11-23"},
        {"max_salary": 5000, "min_salary": 2000, "date_posted": "2001-02-15"},
    ]


def test_sort_by_criteria(jobs):
    sort_by(jobs, "max_salary")
    assert [
        {"max_salary": 20000, "min_salary": 1200, "date_posted": "2001-10-02"},
        {"max_salary": 15000, "min_salary": 5000, "date_posted": "2001-11-23"},
        {"max_salary": 5000, "min_salary": 2000, "date_posted": "2001-02-15"},
    ] == jobs

    sort_by(jobs, "min_salary")
    assert [
        {"max_salary": 5000, "min_salary": 2000, "date_posted": "2001-02-15"},
        {"max_salary": 15000, "min_salary": 5000, "date_posted": "2001-11-23"},
        {"max_salary": 20000, "min_salary": 1200, "date_posted": "2001-10-02"},
    ] == jobs

    sort_by(jobs, "date_posted")
    assert [
        {"max_salary": 5000, "min_salary": 2000, "date_posted": "2001-02-15"},
        {"max_salary": 20000, "min_salary": 1200, "date_posted": "2001-10-02"},
        {"max_salary": 15000, "min_salary": 5000, "date_posted": "2001-11-23"},
    ] == jobs

from src.sorting import sort_by
import pytest


jobs_test = [
    {"min_salary": 100, "max_salary": 300, "date_posted": "2021-05-03"},
    {"min_salary": 200, "max_salary": 400, "date_posted": "2021-05-02"},
    {"min_salary": 300, "max_salary": 500, "date_posted": "2021-05-01"},
]


expect_min_salary = [
    {"min_salary": 100, "max_salary": 300, "date_posted": "2021-05-03"},
    {"min_salary": 200, "max_salary": 400, "date_posted": "2021-05-02"},
    {"min_salary": 300, "max_salary": 500, "date_posted": "2021-05-01"},
]


expect_max_salary = [
    {"min_salary": 300, "max_salary": 500, "date_posted": "2021-05-01"},
    {"min_salary": 200, "max_salary": 400, "date_posted": "2021-05-02"},
    {"min_salary": 100, "max_salary": 300, "date_posted": "2021-05-03"},
]


expect_date_posted = [
    {"min_salary": 100, "max_salary": 300, "date_posted": "2021-05-03"},
    {"min_salary": 200, "max_salary": 400, "date_posted": "2021-05-02"},
    {"min_salary": 300, "max_salary": 500, "date_posted": "2021-05-01"},
]


def test_sort_by_criteria():
    pass

    sort_by(jobs_test, "min_salary")
    assert jobs_test == expect_min_salary

    sort_by(jobs_test, "max_salary")
    assert jobs_test == expect_max_salary

    sort_by(jobs_test, "date_posted")
    assert jobs_test == expect_date_posted

    with pytest.raises(ValueError):
        sort_by(jobs_test, "invalid_criteria")

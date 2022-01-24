from src.sorting import sort_by

import pytest

jobs_mock = [
    {"min_salary": 2000, "max_salary": 5000, "date_posted": "2020-05-05"},
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2020-06-06"},
    {"min_salary": 5000, "max_salary": 9000, "date_posted": "2020-04-04"},
    {"min_salary": 1000, "max_salary": 7000, "date_posted": "2020-03-03"},
]

expect_min = [
    {"min_salary": 1000, "max_salary": 7000, "date_posted": "2020-03-03"},
    {"min_salary": 2000, "max_salary": 5000, "date_posted": "2020-05-05"},
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2020-06-06"},
    {"min_salary": 5000, "max_salary": 9000, "date_posted": "2020-04-04"},
]

expect_max = [
    {"min_salary": 5000, "max_salary": 9000, "date_posted": "2020-04-04"},
    {"min_salary": 1000, "max_salary": 7000, "date_posted": "2020-03-03"},
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2020-06-06"},
    {"min_salary": 2000, "max_salary": 5000, "date_posted": "2020-05-05"},
]

expect_date = [
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2020-06-06"},
    {"min_salary": 2000, "max_salary": 5000, "date_posted": "2020-05-05"},
    {"min_salary": 5000, "max_salary": 9000, "date_posted": "2020-04-04"},
    {"min_salary": 1000, "max_salary": 7000, "date_posted": "2020-03-03"},
]


def test_sort_by_criteria():
    sort_by(jobs_mock, "min_salary")
    assert jobs_mock == expect_min

    sort_by(jobs_mock, "max_salary")
    assert jobs_mock == expect_max

    sort_by(jobs_mock, "date_posted")
    assert jobs_mock == expect_date

    with pytest.raises(ValueError):
        sort_by(jobs_mock, "invalid_data")
    pass

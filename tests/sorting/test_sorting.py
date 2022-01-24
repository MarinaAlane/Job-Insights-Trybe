import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"max_salary": 500, "min_salary": 50, "date_posted": "2021-08-22"},
        {"max_salary": 100, "min_salary": 10, "date_posted": "2020-07-12"},
        {"max_salary": "", "min_salary": "", "date_posted": ""},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2022-01-05"},
        {"max_salary": 15000, "min_salary": 0, "date_posted": "2020-06-02"},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == [
        {"max_salary": 15000, "min_salary": 0, "date_posted": "2020-06-02"},
        {"max_salary": 100, "min_salary": 10, "date_posted": "2020-07-12"},
        {"max_salary": 500, "min_salary": 50, "date_posted": "2021-08-22"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2022-01-05"},
        {"max_salary": "", "min_salary": "", "date_posted": ""},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == [
        {"max_salary": 15000, "min_salary": 0, "date_posted": "2020-06-02"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2022-01-05"},
        {"max_salary": 500, "min_salary": 50, "date_posted": "2021-08-22"},
        {"max_salary": 100, "min_salary": 10, "date_posted": "2020-07-12"},
        {"max_salary": "", "min_salary": "", "date_posted": ""},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2022-01-05"},
        {"max_salary": 500, "min_salary": 50, "date_posted": "2021-08-22"},
        {"max_salary": 100, "min_salary": 10, "date_posted": "2020-07-12"},
        {"max_salary": 15000, "min_salary": 0, "date_posted": "2020-06-02"},
        {"max_salary": "", "min_salary": "", "date_posted": ""},
    ]

    invalid_types = [None, ""]
    for invalid in invalid_types:
        with pytest.raises(ValueError):
            sort_by(jobs, invalid)
from src.sorting import sort_by
import pytest

mock = [
     {"min_salary": 20, "max_salary": 40, "date_posted": "2022-03-01"},
     {"min_salary": 10, "max_salary": 60, "date_posted": "2022-01-01"},
     {"min_salary": 30, "max_salary": 50, "date_posted": "2022-02-01"},
]

expect_min_salary = [
     {"min_salary": 10, "max_salary": 60, "date_posted": "2022-01-01"},
     {"min_salary": 20, "max_salary": 40, "date_posted": "2022-03-01"},
     {"min_salary": 30, "max_salary": 50, "date_posted": "2022-02-01"},
]

expect_max_salary = [
     {"min_salary": 10, "max_salary": 60, "date_posted": "2022-01-01"},
     {"min_salary": 30, "max_salary": 50, "date_posted": "2022-02-01"},
     {"min_salary": 20, "max_salary": 40, "date_posted": "2022-03-01"},
]

expect_date_posted = [
     {"min_salary": 20, "max_salary": 40, "date_posted": "2022-03-01"},
     {"min_salary": 30, "max_salary": 50, "date_posted": "2022-02-01"},
     {"min_salary": 10, "max_salary": 60, "date_posted": "2022-01-01"},
]


def test_sort_by_criteria():
    pass
    sort_by(mock, "min_salary")
    assert mock == expect_min_salary

    sort_by(mock, "max_salary")
    assert mock == expect_max_salary

    sort_by(mock, "date_posted")
    assert mock == expect_date_posted

    with pytest.raises(ValueError):
        sort_by(mock, "invalid_criteria")

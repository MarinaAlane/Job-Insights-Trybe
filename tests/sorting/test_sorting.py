from src.sorting import sort_by
import pytest

mock = [
    {"min_salary": 10, "max_salary": 25, "date_posted": "2021-03-01"},
    {"min_salary": 20, "max_salary": 35, "date_posted": "2021-02-01"},
    {"min_salary": 15, "max_salary": 30, "date_posted": "2021-01-01"},
]


def test_min_salary():
    sort_by(mock, "min_salary")

    expect = [
        {"min_salary": 10, "max_salary": 25, "date_posted": "2021-03-01"},
        {"min_salary": 15, "max_salary": 30, "date_posted": "2021-01-01"},
        {"min_salary": 20, "max_salary": 35, "date_posted": "2021-02-01"},
    ]

    assert mock == expect


def test_max_salary():
    sort_by(mock, "max_salary")

    expect = [
        {"min_salary": 20, "max_salary": 35, "date_posted": "2021-02-01"},
        {"min_salary": 15, "max_salary": 30, "date_posted": "2021-01-01"},
        {"min_salary": 10, "max_salary": 25, "date_posted": "2021-03-01"},
    ]

    assert mock == expect


def test_date_post():
    sort_by(mock, "date_posted")

    expect = [
        {"min_salary": 10, "max_salary": 25, "date_posted": "2021-03-01"},
        {"min_salary": 20, "max_salary": 35, "date_posted": "2021-02-01"},
        {"min_salary": 15, "max_salary": 30, "date_posted": "2021-01-01"},
    ]

    assert mock == expect


def test_sort_by_criteria():
    test_min_salary()
    test_max_salary()
    test_date_post()

    with pytest.raises(ValueError):
        sort_by(mock, "invalid_criteria")
